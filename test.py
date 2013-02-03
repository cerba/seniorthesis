# Test Document for week1.py

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
canvas = r.TCanvas()
#canvas.Divide(2,2)

leg = r.TLegend(0.7,0.7,1,1)
leg.SetHeader = ("Plot Type")


# Define Histogram
gluplot = r.TH1D('Gluon Transverse Momentum','',100,0,100)


# Fill Histogram
glulist = []

for j in range(tree.GetEntries()) :
    tree.GetEntry(j)
    for i in range(0,16) :
        if tree.genPdgId[i] == 21 :
            glulist.append(tree.genP4[i].pt())

print glulist
'''
for iEvent in range(tree.GetEntries()) :
    tree.GetEntry(iEvent)
    for i in range(tree.genP4.GetEntries()):
        glulist.append(tree.genP4
#    tree.GetCoordinates()
#    gluplot.Fill(tree.genP4.pt())


# Plot Histogram

#canvas.cd(1)
gluplot.Draw()
canvas.Print('%s.pdf'%fileName)

'''

#End Program
print 'End of Program'
