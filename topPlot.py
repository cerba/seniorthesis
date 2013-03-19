# Test Document for angplot.py: use one file to try filling histograms

import sys
import setuproot
import ROOT as r
r.gInterpreter.GenerateDictionary('vector<ROOT::Math::LorentzVector<ROOT::Math::PtEtaPhiM4D<Double32_t> > >','vector;Math/LorentzVector.h')

# Open File
f = r.TFile.Open("root://xrootd.grid.hep.ph.ic.ac.uk///store/user/bbetchar/TOP/automated/2013_01_15_05_13_16/TT_CT10_TuneZ2star_8TeV-powheg-tauola.Summer12_DR53X-PU_S10_START53_V7A-v1.AODSIM/topTuple_21_1_q59.root")

tree = f.Get('topRef/tree')

# Define Histogram
gluplot = r.TH1D('Leading Gluon Transverse Momentum','g,p_T',100,0,450)
btplot = r.TH1D('Top from Gluon Pt','t;p_t',100,0,450) #Top from glu
ctplot = r.TH1D('Top from Quarks Pt','t;p_t',100,0,450) #Top from quarks
xtplot = r.TH1D('Anti-Top from Gluon Pt','#bar{t};p_T',100,0,450) #Anti-Top from glu
ytplot = r.TH1D('Anti-Top from Quarks Pt','#bar{t};p_T',100,0,450) #Anti-Top from quarks

glubtAngl = r.TH1D('Cos Theta Glu vs T from Glu','',100,-1,1)
gluctAngl = r.TH1D('Cos Theta Glu vs T from Q/QBar','',100,-1,1)
gluxTbarAngl = r.TH1D('Cos Theta Glu vs TBar from Glu','',100,-1,1)
gluyTbarAngl = r.TH1D('Cos Theta Glu vs TBar from Q/QBar','',100,-1,1)

# Fill Histogram

for j in range(tree.GetEntries()) :
    tree.GetEntry(j)
    index = range(len(tree.genPdgId))
    glu = next((i for i in index if tree.genPdgId[i] == 21 and tree.genMotherIndex[i] == 4), None)
    bt = next((i for i in index if tree.genPdgId[i] == 6 and tree.genMotherPdgId[i] == 21), None)
    ct = next((i for i in index if tree.genPdgId[i] == 6 and tree.genMotherPdgId[i] <=5 and tree.genMotherPdgId[i] >= -5), None)
    xt = next((i for i in index if tree.genPdgId[i] == -6 and tree.genMotherPdgId[i] == 21), None)
    yt = next((i for i in index if tree.genPdgId[i] == -6 and tree.genMotherPdgId[i] <=5 and tree.genMotherPdgId[i] >= -5), None)
    
    if glu!=None :
        gluplot.Fill(tree.genP4[glu].pt())
    if glu!=None and bt!=None :
        glubtAngl.Fill(r.Math.VectorUtil.CosTheta(tree.genP4[glu],tree.genP4[bt]))
    if glu!=None and ct!=None :
        gluctAngl.Fill(r.Math.VectorUtil.CosTheta(tree.genP4[glu],tree.genP4[ct]))
    if glu!=None and xt!=None :
        gluxTbarAngl.Fill(r.Math.VectorUtil.CosTheta(tree.genP4[glu],tree.genP4[xt]))
    if glu!=None and yt!=None :
        gluyTbarAngl.Fill(r.Math.VectorUtil.CosTheta(tree.genP4[glu],tree.genP4[yt]))

    if  bt!=None :
        btplot.Fill(tree.genP4[bt].pt())
    if  ct!=None :
        ctplot.Fill(tree.genP4[ct].pt())
    if xt!=None :
        xtplot.Fill(tree.genP4[xt].pt())
    if yt!=None :
        ytplot.Fill(tree.genP4[yt].pt())

# Plot Histogram

canvas = r.TCanvas()
fileName = 'topPlots.pdf'
leg = r.TLegend(0.7,0.7,1,1)
leg.SetHeader = ("Plot Type")

canvas.Print(fileName + '[') # open for multipage printing

for hist in [gluplot, btplot, ctplot, xtplot, ytplot, glubtAngl, gluctAngl, gluxTbarAngl, gluyTbarAngl] :
    hist.Draw()
    canvas.Print(fileName)
canvas.Print(fileName + ']') # close for multipage printing

# End Program
print 'End of Program'
