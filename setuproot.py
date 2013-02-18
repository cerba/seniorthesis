import os
import ROOT as r


def cppROOTDictionariesToGenerate() :
        return [
            ("pair<string,bool>", "string"),
            ("map<std::string,bool>", "string;map"),
            ("pair<string,string>", "string"),
            ("map<std::string,string>", "string;map"),
            ("ROOT::Math::Cartesian3D<float>", "Math/Point3D.h"),
            ("ROOT::Math::DisplacementVector3D<ROOT::Math::Cartesian3D<float>,ROOT::Math::DefaultCoordinateSystemTag>", "Math/Vector3D.h"),
            ("vector<ROOT::Math::DisplacementVector3D<ROOT::Math::Cartesian3D<float>,ROOT::Math::DefaultCoordinateSystemTag> >", "vector;Math/Vector3D.h"),
            ("ROOT::Math::PositionVector3D<ROOT::Math::Cartesian3D<float>,ROOT::Math::DefaultCoordinateSystemTag>", "Math/Point3D.h"),
            ("vector<ROOT::Math::PositionVector3D<ROOT::Math::Cartesian3D<float>,ROOT::Math::DefaultCoordinateSystemTag> >", "vector;Math/Point3D.h"),
            #ROOT::Math::LorentzVector<ROOT::Math::PtEtaPhiM4D<float> > etc. is addressed in linkdef.cxx
            #('vector<ROOT::Math::LorentzVector<ROOT::Math::PtEtaPhiM4D<Double32_t> > >','vector;Math/LorentzVector.h')
            ("vector<ROOT::Math::LorentzVector<ROOT::Math::PtEtaPhiM4D<float> > >", "vector;Math/LorentzVector.h"),
            ("vector< vector< float > >", "vector"),
            ("vector< vector< unsigned int> >", "vector"),
            ("vector< vector< int> >", "vector"),
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
            
initializeROOT(r,["linkdef.cxx"])
