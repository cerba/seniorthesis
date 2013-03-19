# First Attempt at Kinematics Analysis

import sys
import setuproot
import ROOT as r
r.gInterpreter.GenerateDictionary('vector<ROOT::Math::LorentzVector<ROOT::Math::PtEtaPhiM4D<Double32_t> > >','vector;Math/LorentzVector.h')

# Open File

f = r.TFile.Open("root://xrootd.grid.hep.ph.ic.ac.uk///store/user/bbetchar/TOP/automated/2013_01_15_05_13_16/TT_CT10_TuneZ2star_8TeV-powheg-tauola.Summer12_DR53X-PU_S10_START53_V7A-v1.AODSIM/topTuple_21_1_q59.root")

tree = f.Get('topRef/tree')

# Define Histogram
jetplot = r.TH1D('Jet PTs','',100,0,450)
muplot = r.TH1D('Muon PTs','',100,0,450)
elplot = r.TH1D('Electron PTs','',100,0,450)

# Make Selection Cuts

#jetIndices = [4,5]

for i in range(0,5) : #range(tree.GetEntries()) :
    if tree.jetP4[i] >= 4 and elRelIso[i] < 0.1 :
        elplot.Fill(tree.electronP4[i].pt())
    if tree.jetP4[i] >= 4 and muRelIso[i] < 0.12 :
        muplot.Fill(muP4[i].pt())


#jetplot.Fill()

# Plot Histogram

canvas = r.TCanvas()
fileName = 'kinetest.pdf'
leg = r.TLegend(0.7,0.7,1,1)
leg.SetHeader = ("Plot Type")

canvas.Print(fileName + '[') # open for multipage printing

for hist in [elplot, muplot] :
        hist.Draw()
        canvas.Print(fileName)
canvas.Print(fileName + ']') # close for multipage printing


# End Program
print 'End of Program'
