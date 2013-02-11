import os
import ROOT as r


def cppROOTDictionariesToGenerate() :
    return [
        ('vector<ROOT::Math::LorentzVector<ROOT::Math::PtEtaPhiM4D<Double32_t> > >','vector;Math/LorentzVector.h')
        ]

def generateDictionaries(inList, dir = None) :
    '''http://root.cern.ch/drupal/content/how-generate-dictionary'''
    wd = os.getcwd()
    r.gSystem.ChangeDirectory((dir if dir!=None else wd)+"/cpp")
    for item in inList : r.gInterpreter.GenerateDictionary(*item)
    r.gSystem.ChangeDirectory(wd)

def initializeROOT(r, cppFiles = []) :
    r.gROOT.SetStyle("Plain")
    r.gStyle.SetPalette(1)
    r.TH1.SetDefaultSumw2(True)
    r.gErrorIgnoreLevel = 2000
    r.gROOT.SetBatch(True)
    
    for sourceFile in cppFiles :
        r.gROOT.LoadMacro(sourceFile+"+")
        
        
generateDictionaries(cppROOTDictionariesToGenerate())
        
initializeROOT(r,["cpp/linkdef.cxx"])
        
