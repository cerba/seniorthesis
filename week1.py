### Week 1 Assignment: Opening Angle Plots

import ROOT as r
r.gROOT.SetBatch(1)
r.gInterpreter.GenerateDictionary('vector<ROOT::Math::LorentzVector<ROOT::Math::PtEtaPhiM4D<Double32_t> > >','vector;Math/LorentzVector.h')


# open files, read their names, and string them tog in chain
f = open('ttj_ph.txt')
filenames = f.readlines()
#chain = r.TChain('topRef/tree')
#tfile = r.TFile.Open(filenames[0])
tfile = r.TNetFile(filenames[0])
tree = tfile.Get('topRef/tree')
chain = r.TChain()
chain.Add(tree)


#chain.Add(filenames[0])

for i in range(chain.GetEntries()) :
    chain.GetEntry(i)
    for j in range(len(chain.genPdgId)) :
        print j, chain.genPdgId[j], chain.genP4[j].pt(), chain.genP4[j].eta(), chain.genMotherPdgId[j], chain.genMotherIndex[j]
        

'''
# Make Histograms

canvas = r.TCanvas()
canvas.Divide(2,2)

leg = r.TLegend(0.7,0.7,1,1)
leg.SetHeader = ("Plot Type")


#Print Canvas

for i, h in enum(histos + [plot1, plot2, plot3] ):
    h.SetLineColor(i+3)
    canvas.cd(i+1)
    h.Draw()

canvas.Print()
'''

print 'End of Program'
    
    
