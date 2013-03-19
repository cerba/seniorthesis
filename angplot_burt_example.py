import setuproot,time
import ROOT as r
r.gInterpreter.GenerateDictionary('vector<ROOT::Math::LorentzVector<ROOT::Math::PtEtaPhiM4D<Double32_t> > >','vector;Math/LorentzVector.h')

# Define Histograms
g_pt = r.TH1D('gpt','g;p_T',100,0,100)
b_pt = r.TH1D('bpt','b;p_T',100,0,100)
bbar_pt = r.TH1D('b_pt','#bar{b};p_T',100,0,100)
gtopCosTheta = r.TH1D('angGTop','gluon-top;cos#theta',100,-1,1)
gantitopCosTheta = r.TH1D('angGTbar','gluon-#bar{t};cos#theta',100,-1,1)

# Open File
f = r.TFile.Open("root://xrootd.grid.hep.ph.ic.ac.uk///store/user/bbetchar/TOP/automated/2013_01_15_05_13_16/TT_CT10_TuneZ2star_8TeV-powheg-tauola.Summer12_DR53X-PU_S10_START53_V7A-v1.AODSIM/topTuple_21_1_q59.root")
tree = f.Get('topRef/tree')

power = 0
for iEntry in range(tree.GetEntries()) :
    if iEntry == 2**power :
        if not power : start = time.time()
        print "Seconds: %d\tEvents: %d"%(time.time()-start, iEntry)
        power += 1
    tree.GetEntry(iEntry)
    indices = range(len(tree.genPdgId))
    iGlu = next((i for i in indices if tree.genPdgId[i]==21 and tree.genMotherIndex[i]==4),None) # default to None if there are no gluons
    iB = next(i for i in indices if tree.genPdgId[i]==5)
    iB_= next(i for i in indices if tree.genPdgId[i]==-5)
    iT = next(i for i in indices if tree.genPdgId[i]==6)
    iT_ = next(i for i in indices if tree.genPdgId[i]==-6)

    if iGlu!=None :
        g_pt.Fill(tree.genP4[iGlu].pt())
        gtopCosTheta.Fill( r.Math.VectorUtil.CosTheta(tree.genP4[iGlu], tree.genP4[iT]) )
        gantitopCosTheta.Fill( r.Math.VectorUtil.CosTheta(tree.genP4[iGlu], tree.genP4[iT_] ))
        
    b_pt.Fill(tree.genP4[iB].pt())
    bbar_pt.Fill(tree.genP4[iB_].pt())
            
            
canvas = r.TCanvas()
fileName = 'burt_example.pdf'
canvas.Print(fileName + '[') # open for multipage printing
            
for hist in [g_pt, b_pt, bbar_pt, gtopCosTheta, gantitopCosTheta] :
    hist.Draw()
    canvas.Print(fileName)
canvas.Print(fileName + ']') # close for multipage printing
print "Wrote %s"%fileName
