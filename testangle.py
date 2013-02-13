# Test Document for modangplot.py

import sys
import setuproot
import ROOT as r
r.gInterpreter.GenerateDictionary('vector<ROOT::Math::LorentzVector<ROOT::Math::PtEtaPhiM4D<Double32_t> > >','vector;Math/LorentzVector.h')

# Open File
f = r.TFile.Open("root://xrootd.grid.hep.ph.ic.ac.uk///store/user/bbetchar/TOP/automated/2013_01_15_05_13_16/TT_CT10_TuneZ2star_8TeV-powheg-tauola.Summer12_DR53X-PU_S10_START53_V7A-v1.AODSIM/topTuple_21_1_q59.root")

tree = f.Get('topRef/tree')

# Define Histogram
gluplot = r.TH1D('Gluon Transverse Momentum','g,p_T',100,0,450)
tplot = r.TH1D('Top Transverse Momentum','t;p_t',100,0,450)
atplot = r.TH1D('Anti-Top Transverse Momentum','#bar{t};p_T',100,0,450)
qwplot = r.TH1D('Q from W+ Transverse Momentum','',100,0,450)
aqwplot = r.TH1D('Q from W- Transverse Momentum','',100,0,450)

qwlist = []
aqwlist = []
tlist = []
atlist = []
qw = 0 

# Fill Histogram

for j in range(0,1) : #range(tree.GetEntries()) :
    tree.GetEntry(j)
    index = range(len(tree.genPdgId))
    glu = next((i for i in index if tree.genPdgId[i] == 21 and tree.genMotherIndex[i] == 4), None)
#    qw = next((i for i in index if tree.genMotherPdgId[i] == 24 and tree.genPdgId[i] == 1 or tree.genPdgId[i] == 2 or tree.genPdgId[i] == 3 or tree.genPdgId[i] == 4 or tree.genPdgId[i] == 5 or tree.genPdgId[i] == 6), None)
     #   aqw = next((i for i in index if tree.genMotherPdgId[i] == -24 and tree.genPdgId[i] == -1 or tree.genPdgId[i] == -2 or tree.genPdgId[i] == -3 or tree.genPdgId[i] == -4 or tree.genPdgId[i] == -5 or tree.genPdgId[i] == -6), None)
    for i in range(0,2) :
        qw = ( next(i for i in index if tree.genMotherPdgId[i] == 24))
    aqw = next((i for i in index if tree.genMotherPdgId[i] == -24), None)
    t = next((i for i in index if tree.genPdgId[i] == 6), None)
    at = next((i for i in index if tree.genPdgId[i] == -6), None)

    qwlist.append(qw)
    aqwlist.append(aqw)
    tlist.append(t)
    atlist.append(at)

    if glu!=None :
        gluplot.Fill(tree.genP4[glu].pt())
                
    qwplot.Fill(tree.genP4[qw].pt())
    aqwplot.Fill(tree.genP4[aqw].pt())

print qwlist
print aqwlist
print tlist
print atlist

'''
# Plot Histogram

canvas = r.TCanvas()
fileName = 'testangle.pdf'
leg = r.TLegend(0.7,0.7,1,1)
leg.SetHeader = ("Plot Type")

canvas.Print(fileName + '[') # open for multipage printing

for hist in [qwplot, aqwplot] :
    hist.Draw()
    canvas.Print(fileName)
canvas.Print(fileName + ']') # close for multipage printing
'''
# End Program
print 'End of Program'
