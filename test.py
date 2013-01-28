import sys
import ROOT as r
r.gROOT.SetBatch(1)

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
canvas.Divide(2,2)

leg = r.TLegend(0.7,0.7,1,1)
leg.SetHeader = ("Plot Type")

# Define Histogram
gluP4 = r.TH1D('Gluon Transverse Momentum','',10,0,10)


# Fill Histogram

#for i in tree.Row :
if tree.genPdgId == 21 :
    gluP4.Fill(genP4.pt())



# Plot Histogram
canvas.cd(1)
gluP4.Draw()
canvas.Print('%s.pdf'%fileName)





#End Program
print 'End of Program'


