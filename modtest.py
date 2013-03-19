# Modified Test Document for week1.py: clean up and organize code from test.py

import sys
import setuproot
import ROOT as r
r.gROOT.SetBatch(1)
r.gInterpreter.GenerateDictionary('vector<ROOT::Math::LorentzVector<ROOT::Math::PtEtaPhiM4D<Double32_t> > >','vector;Math/LorentzVector.h')

# Define a File Name for Histogram
if len(sys.argv)<2 :
    print  "Please provide an output file name."
    sys.exit(0)
    
fileName = sys.argv[1]


# Open File
f = r.TFile.Open("root://xrootd.grid.hep.ph.ic.ac.uk///store/user/bbetchar/TOP/automated/2013_01_15_05_13_16/TT_CT10_TuneZ2star_8TeV-powheg-tauola.Summer12_DR53X-PU_S10_START53_V7A-v1.AODSIM/topTuple_21_1_q59.root")

tree = f.Get('topRef/tree')


# Make Canvas, Set Legend
c1 = r.TCanvas()
c2 = r.TCanvas()
c1.Divide(2,2)
c2.Divide(2,2)

leg = r.TLegend(0.7,0.7,1,1)
leg.SetHeader = ("Plot Type")


# Define Histogram

plotnames = ['Gluon','Proton','Top','Anti-Top','Bottom','Anti-Bottom','Q from W+','Q from W-']

histos = [r.TH1D('%s Transverse Momentum'%name,'',100,0,100) for name in plotnames]

# Fill Histogram

listnames = ['glulist','prolist','tlist','atlist','blist','ablist','qwlist','aqwlist']

for name in listnames:
    list = '%s'%name
    list = []

for j in range(tree.GetEntries()) :
    tree.GetEntry(j)
    for i in range(len(tree.genPdgId)) :
        if tree.genPdgId[i] == 21 and tree.genMotherIndex[i] == 4:
            list[0].append(tree.genP4[i].pt())
                
    for i in range(2,15) :
        if tree.genPdgId[i] == 2212 :
            list[1].append(tree.genP4[i].pt())
   
    for i in range(0,16) :
        if tree.genPdgId[i] == 6 :
            list[2].append(tree.genP4[i].pt())
        if tree.genPdgId[i] == -6 :
            list[3].append(tree.genP4[i].pt())
        if tree.genPdgId[i] == 5 :
            list[4].append(tree.genP4[i].pt())
        if tree.genPdgId[i] == -5 :
            list[5].append(tree.genP4[i].pt())

    for i in range(0,15) :
        if tree.genPdgId[i] == 24 and tree.genPdgId[i+1] == 1 or tree.genPdgId[i+1] == 2 or tree.genPdgId[i+1] == 3 or tree.genPdgId[i+1] == 4 or tree.genPdgId[i+1] == 5 or tree.genPdgId[i+1] == 6:
            list[6].append(tree.genP4[i+1].pt())

        if tree.genPdgId[i] == -24 and tree.genPdgId[i+1] == 1 or tree.genPdgId[i+1] == 2 or tree.genPdgId[i+1] == 3 or tree.genPdgId[i+1] == 4 or tree.genPdgId[i+1] == 5 or tree.genPdgId[i+1] == 6:
            list[7].append(tree.genP4[i+1].pt())
                                                            
for i in range(0,len(list[i]) - 1):
        histos[i].Fill(list[i])

print list[0]

# Plot Histogram

for i in range(1,9) :
    c[i].cd(i)
    list[i].Draw()
    
c1.Print('%s.pdf'%fileName)
c2.Print('%s_2.pdf'%fileName)

# End Program
print 'End of Program'
