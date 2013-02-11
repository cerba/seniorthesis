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
bplot = r.TH1D('Bottom Transverse Momentum','b;p_t',100,0,450)
abplot = r.TH1D('Anti-Bottom Transverse Momentum','#bar{b};p_T',100,0,450)
tplot = r.TH1D('Top Transverse Momentum','t;p_t',100,0,450)
atplot = r.TH1D('Anti-Top Transverse Momentum','#bar{t};p_T',100,0,450)
qwplot = r.TH1D('Q from W+ Transverse Momentum','',100,0,450)
aqwplot = r.TH1D('Q from W- Transverse Momentum','',100,0,450)
igluplot = r.TH1D('Gluon First P Transverse Momentum','g,p_T',100,0,450)
ingluplot = r.TH1D('Gluon Second P Transverse Momentum','g,p_T',100,0,450)



glubAngl = r.TH1D('Open Angle Gluon vs. B','',100,-1,1)
gluBbarAngl = r.TH1D('Open Angle Gluon vs. Bbar','',100,-1,1)
glutAngl = r.TH1D('Open Angle Gluon vs. t','',100,-1,1)
gluTbarAngl = r.TH1D('Open Angle Gluon vs. tbar','',100,-1,1)
gluQwAngl = r.TH1D('Open Angle Gluon vs. QW+','',100,-1,1)
gluAqwAngl = r.TH1D('Open Angle Gluon vs. QW-','',100,-1,1)
gluipAngl = r.TH1D('Open Angle Gluon vs. P1','',100,-1,1)
gluinpAngl = r.TH1D('Open Angle Gluon vs. P2','',100,-1,1)



# Fill Histogram

for j in range(tree.GetEntries()) :
    tree.GetEntry(j)
    index = range(len(tree.genPdgId))
    glu = next((i for i in index if tree.genPdgId[i] == 21 and tree.genMotherIndex[i] == 4), None)
    b = next((i for i in index if tree.genPdgId[i] == 5 and tree.genMotherIndex[i] == 6), None)
    ab = next(( i for i in index if tree.genPdgId[i] == -5 and tree.genMotherIndex[i] == 7), None)
    t = next((i for i in index if tree.genPdgId[i] == 6), None)
    at = next((i for i in index if tree.genPdgId[i] == -6), None)
    qw = next((i for i in index if tree.genMotherPdgId[i] == 24 and tree.genPdgId[i] == 1 or tree.genPdgId[i] == 2 or tree.genPdgId[i] == 3 or tree.genPdgId[i] == 4 or tree.genPdgId[i] == 5 or tree.genPdgId[i] == 6), None)          
    aqw = next((i for i in index if tree.genMotherPdgId[i] == -24 and tree.genPdgId[i] == -1 or tree.genPdgId[i] == -2 or tree.genPdgId[i] == -3 or tree.genPdgId[i] == -4 or tree.genPdgId[i] == -5 or tree.genPdgId[i] == -6), None)          
    iglu = next((i for i in index if tree.genPdgId[i] == 21 and tree.genMotherIndex[i] == 0),None)
    inglu = next((i for i in index if tree.genPdgId[i] == 21 and tree.genMotherIndex[i] == 1),None)
    
    if glu!=None and iglu!=None and inglu!=None :
        gluplot.Fill(tree.genP4[glu].pt())
        glubAngl.Fill(r.Math.VectorUtil.CosTheta(tree.genP4[glu],tree.genP4[b]))
        gluBbarAngl.Fill(r.Math.VectorUtil.CosTheta(tree.genP4[glu],tree.genP4[ab]))
        glutAngl.Fill(r.Math.VectorUtil.CosTheta(tree.genP4[glu],tree.genP4[t]))
        gluTbarAngl.Fill(r.Math.VectorUtil.CosTheta(tree.genP4[glu],tree.genP4[at]))
        gluQwAngl.Fill(r.Math.VectorUtil.CosTheta(tree.genP4[glu],tree.genP4[qw]))
        gluAqwAngl.Fill(r.Math.VectorUtil.CosTheta(tree.genP4[glu],tree.genP4[aqw]))
        gluipAngl.Fill(r.Math.VectorUtil.CosTheta(tree.genP4[glu],tree.genP4[iglu]))
        gluinpAngl.Fill(r.Math.VectorUtil.CosTheta(tree.genP4[glu],tree.genP4[inglu]))
        

    bplot.Fill(tree.genP4[b].pt())
    abplot.Fill(tree.genP4[ab].pt())
    tplot.Fill(tree.genP4[t].pt())
    atplot.Fill(tree.genP4[at].pt())
    qwplot.Fill(tree.genP4[qw].pt())
    aqwplot.Fill(tree.genP4[aqw].pt())
#for i in range(len(tree.genPdgId) - 1) :
    
    
# Plot Histogram

canvas = r.TCanvas()
fileName = 'openangle.pdf'
leg = r.TLegend(0.7,0.7,1,1)
leg.SetHeader = ("Plot Type")

canvas.Print(fileName + '[') # open for multipage printing

for hist in [gluplot, bplot, abplot, tplot, atplot, qwplot, aqwplot, glubAngl, gluBbarAngl, glutAngl, gluTbarAngl, gluQwAngl, gluAqwAngl, gluipAngl, gluinpAngl] :
    hist.Draw()
    canvas.Print(fileName)
canvas.Print(fileName + ']') # close for multipage printing

# End Program
print 'End of Program'
