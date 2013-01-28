### Week 1 Assignment: Opening Angle Plots

import ROOT as r
r.gROOT.SetBatch(1)

# open files, read their names, and string them tog in chain
f = open('ttj_ph.txt')
filenames = f.readlines()
chain = r.TChain('topRef/tree')

for f in filenames:
    file  = r.TFile.Open(f)
    chain.Add('file')

print chain.GetEntry(0)

'''
chain = r.TChain('topRef/tree')

for f in filenames:
    g = r.TFile.Open(f)
    
    chain.Add(g)
    
    break
#print chain.GetEntries() #slow

chain.GetEntry(0)
for id in chain.genPdgId:
    print id
'''

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
    
    
