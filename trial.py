# Test Document for angplot.py: use one file to try filling histograms

# Test Document for angplot.py: use one file to try filling histograms

import sys
import setuproot
import ROOT as r
r.gInterpreter.GenerateDictionary('vector<ROOT::Math::LorentzVector<ROOT::Math::PtEtaPhiM4D<Double32_t> > >','vector;Math/LorentzVector.h')

# Open File
f = r.TFile.Open("root://xrootd.grid.hep.ph.ic.ac.uk///store/user/bbetchar/TOP/automated/2013_01_15_05_13_16/TT_CT10_TuneZ2star_8TeV-powheg-tauola.Summer12_DR53X-PU_S10_START53_V7A-v1.AODSIM/topTuple_21_1_q59.root")

tree = f.Get('topRef/tree')

# Define Histogram
gluplot = r.TH1D('Gluon Transverse Momentum','g,p_T',100,0,450)
qwplot = r.TH1D('Q from W+ Transverse Momentum','',100,0,450)
aqwplot = r.TH1D('Q from W- Transverse Momentum','',100,0,450)

gluQwAngl = r.TH1D('Open Angle Gluon vs. QW+','',100,-1,1)
gluAqwAngl = r.TH1D('Open Angle Gluon vs. QW-','',100,-1,1)



# Fill Histogram

for j in range(0,1000): #range(tree.GetEntries()) :
    tree.GetEntry(j)
    index = range(len(tree.genPdgId))
    glu = next((i for i in index if tree.genPdgId[i] == 21 and tree.genMotherIndex[i] == 4), None)
    bqw = next((i for i in index if tree.genMotherPdgId[i] == 24 and tree.genPdgId[i] >= -6 and tree.genPdgId[i] <= 6), 0)
    cqw = next((i for i in index if tree.genMotherPdgId[i-1] == 24 and tree.genMotherPdgId[i] == 24 and tree.genPdgId[i] >= -6 and tree.genPdgId[i] <= 6), 0)
    xqw = next((i for i in index if tree.genMotherPdgId[i] == -24 and tree.genPdgId[i] >= -6 and tree.genPdgId[i] <= 6), 0)
    yqw = next((i for i in index if tree.genMotherPdgId[i-1] == -24 and tree.genMotherPdgId[i] == -24 and tree.genPdgId[i] >= -6 and tree.genPdgId[i] <= 6), 0)

    if glu!=None :
        gluplot.Fill(tree.genP4[glu].pt())
        gluQwAngl.Fill(r.Math.VectorUtil.CosTheta(tree.genP4[glu],tree.genP4[bqw]))
        gluQwAngl.Fill(r.Math.VectorUtil.CosTheta(tree.genP4[glu],tree.genP4[cqw]))
        gluAqwAngl.Fill(r.Math.VectorUtil.CosTheta(tree.genP4[glu],tree.genP4[xqw]))
        gluAqwAngl.Fill(r.Math.VectorUtil.CosTheta(tree.genP4[glu],tree.genP4[yqw]))

    if bqw!=0 : 
        qwplot.Fill(tree.genP4[bqw].pt())
    if cqw!=0 : 
        qwplot.Fill(tree.genP4[cqw].pt())
    if xqw!=0 : 
        aqwplot.Fill(tree.genP4[xqw].pt())
    if yqw!=0 : 
        aqwplot.Fill(tree.genP4[yqw].pt())

'''
# Quark from W Plots

for j in range(tree.GetEntries()) :
tree.GetEntry(j)
for i in range(len(tree.genPdgId)) :
if tree.genMotherPdgId[i] == 24 :
if tree.genPdgId[i] >= -6 and tree.genPdgId[i] <= 6 :
qwlist.append(tree.genP4[i].pt())
elif tree.genPdgId[i] >= -6 and tree.genPdgId[i] <= 6 :
qwlist.append(tree.genP4[i].pt())
if tree.genMotherPdgId[i] == -24 :
if tree.genPdgId[i] >= -6 and tree.genPdgId[i] <= 6 :
aqwlist.append(tree.genP4[i].pt())
elif tree.genPdgId[i] >= -6 and tree.genPdgId[i] <= 6 :
aqwlist.append(tree.genP4[i].pt())

for i in range(0,len(qwlist) - 1):
qwplot.Fill(qwlist[i])

for i in range(0,len(aqwlist) - 1):
aqwplot.Fill(aqwlist[i])
'''

# Plot Histogram

canvas = r.TCanvas()
fileName = 'trial.pdf'
leg = r.TLegend(0.7,0.7,1,1)
leg.SetHeader = ("Plot Type")

canvas.Print(fileName + '[') # open for multipage printing

for hist in [gluplot, qwplot, aqwplot, gluQwAngl, gluAqwAngl] :
    hist.Draw()
    canvas.Print(fileName)
canvas.Print(fileName + ']') # close for multipage printing


# End Program
print 'End of Program'
