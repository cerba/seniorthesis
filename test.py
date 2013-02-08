# Test Document for week1.py: use one file to try filling histograms

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
gluplot = r.TH1D('Gluon Transverse Momentum','',100,0,100)
proplot = r.TH1D('Proton Transverse Momentum','',100,0,100)
tplot = r.TH1D('Top Transverse Momentum','',100,0,100)
atplot = r.TH1D('AntiTop Transverse Momentum','',100,0,100)
bplot = r.TH1D('Bottom Transverse Momentum','',100,0,100)
abplot = r.TH1D('Anti-Bottom Transverse Momentum','',100,0,100)
qwplot = r.TH1D('Q from W+ Transverse Momentum','',100,0,100)
aqwplot = r.TH1D('Q from W- Transverse Momentum','',100,0,100)

# Fill Histogram
glulist = []
prolist = []
tlist = []
atlist = []
blist = []
ablist = []
qwlist = []
aqwlist = []

for j in range(tree.GetEntries()) :
    tree.GetEntry(j)
    for i in range(0,15) :
        if tree.genPdgId[i] == -6 :
            if tree.genPdgId[i+1] == 21 :
                glulist.append(tree.genP4[i+1].pt())
                
                
for i in range(0,len(glulist) - 1):
    gluplot.Fill(glulist[i])

'''
    for i in range(2,15) :
        if tree.genPdgId[i] == 2212 :
            prolist.append(tree.genP4[i].pt())
    proplot.Fill(len(prolist))

    for i in range(0,16) :
        if tree.genPdgId[i] == 6 :
            tlist.append(tree.genP4[i].pt())
    tplot.Fill(len(tlist))

    for i in range(0,16) :
        if tree.genPdgId[i] == -6 :
            atlist.append(tree.genP4[i].pt())
    atplot.Fill(len(atlist))

    for i in range(0,16) :
        if tree.genPdgId[i] == 5 :
            blist.append(tree.genP4[i].pt())
    bplot.Fill(len(blist))

    for i in range(0,16) :
        if tree.genPdgId[i] == -5 :
            ablist.append(tree.genP4[i].pt())
    abplot.Fill(len(ablist))

    for i in range(0,15) :
        if tree.genPdgId[i] == 24 :
            if tree.genPdgId[i+1] == 1 :
                qwlist.append(tree.genP4[i+1].pt())
            if tree.genPdgId[i+1] == 2:
                qwlist.append(tree.genP4[i+1].pt())
            if tree.genPdgId[i+1] == 3 :
                qwlist.append(tree.genP4[i+1].pt())
            if tree.genPdgId[i+1] == 4:
                qwlist.append(tree.genP4[i+1].pt())
            if tree.genPdgId[i+1] == 5 :
                qwlist.append(tree.genP4[i+1].pt())
            if tree.genPdgId[i+1] == 6:
                qwlist.append(tree.genP4[i+1].pt())
    qwplot.Fill(len(qwlist))

    for i in range(0,15) :
        if tree.genPdgId[i] == -24 :
            if tree.genPdgId[i+1] == -1 :
               aqwlist.append(tree.genP4[i+1].pt())
            if tree.genPdgId[i+1] == -2:
                aqwlist.append(tree.genP4[i+1].pt())
            if tree.genPdgId[i+1] == -3 :
                aqwlist.append(tree.genP4[i+1].pt())
            if tree.genPdgId[i+1] == -4:
                aqwlist.append(tree.genP4[i+1].pt())
            if tree.genPdgId[i+1] == -5 :
                aqwlist.append(tree.genP4[i+1].pt())
            if tree.genPdgId[i+1] == -6:
                aqwlist.append(tree.genP4[i+1].pt())
    aqwplot.Fill(len(aqwlist))
'''     
            
print glulist


# Plot Histogram

c1.cd(1)
gluplot.Draw()

'''
c1.cd(2)
proplot.Draw()

c1.cd(3)
tplot.Draw()

c1.cd(4)
atplot.Draw()

c2.cd(1)
bplot.Draw()

c2.cd(2)
abplot.Draw()

c2.cd(3)
qwplot.Draw()

c2.cd(4)
aqwplot.Draw()
'''
c1.Print('%s.pdf'%fileName)
#c2.Print('%s2.pdf'%fileName)


# End Program
print 'End of Program'
