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
c1.Divide(2,2)

leg = r.TLegend(0.7,0.7,1,1)
leg.SetHeader = ("Plot Type")

# Define Histogram
gluplot = r.TH1D('Gluon Transverse Momentum','',100,0,100)
bplot = r.TH1D('Bottom Transverse Momentum','',100,0,100)
abplot = r.TH1D('Anti-Bottom Transverse Momentum','',100,0,100)

# Fill Histogram
glulist = []
blist = []
ablist = []
anglglulist = []
anglblist = []
anglablist = []

for j in range(0,5) :    #range(tree.GetEntries()) :
    tree.GetEntry(j)
    for i in range(len(tree.genPdgId)) :
        if tree.genPdgId[i] == 21 and tree.genMotherIndex[i] == 4 :
            glulist.append(tree.genP4[i].pt())
            anglglulist.append(tree.genP4[i])
        else :  None

        if tree.genPdgId[i] == 5 and tree.genMotherIndex[i] == 6 :
            blist.append(tree.genP4[i].pt())
            anglblist.append(tree.genP4[i])
        else :  None

        if tree.genPdgId[i] == -5 and tree.genMotherIndex[i] == 7 :
            ablist.append(tree.genP4[i].pt())
            anglablist.append(tree.genP4[i])
        else :  None


for i in range(0,len(glulist) - 1):
        gluplot.Fill(glulist[i])

for i in range(0,len(blist) - 1):
        bplot.Fill(blist[i])

for i in range(0,len(ablist) - 1):
        abplot.Fill(ablist[i])

#print glulist

# Open Angle Plots
# Assuming that anglglulist and corresponding particle list are the same size

openangl = []

#for i in range(0,len(anglglulist)) :
   # openangl.append(r.Math.VectorUtil.CosTheta(anglglulist[i],anglblist[i]))

openangl.append(r.Math.VectorUtil.CosTheta(tree.genP4[4],tree.genP4[5]))

anglplot = r.TH1D('Open Angle Gluon vs. B','',100,0,100)

anglplot.Fill(openangl)

c1.cd(4)
anglplot.Draw()

# Plot Histogram

c1.cd(1)
gluplot.Draw()

c1.cd(2)
bplot.Draw()

c1.cd(3)
abplot.Draw()

c1.Print('%s.pdf'%fileName)


# End Program
print 'End of Program'
