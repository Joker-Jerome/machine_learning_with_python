import os 
import pickle

def run(args):
    return(args)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("problem", help="type of analysis (classification/regression/survival)")
    parser.add_argument("input", help="Input folder")
    parser.add_argument("output", help="Output folder")
    parser.add_argument("predictor", help="predictor file")
    parser.add_argument("predictor_set",help="file that specifies predictor group structure")
    parser.add_argument("response",help="outcome data file")
    parser.add_argument("kernel",help="kernel function (rbf/poly3)")
    parser.add_argument("method",help="regularization (L1/L2)")
    parser.add_argument("-clinical",help="file of clinical predictors")
    parser.add_argument("-maxiter",help="maximum number of iteration (default 800)")
    parser.add_argument("-rate",help="learning rate parameter (default 0.05)")
    parser.add_argument("-Lambda",help="penalty parameter")
    parser.add_argument("-test",help="file containing test data index")
    parser.add_argument("-pen",help="penalty multiplier")
    args = parser.parse_args()
    
    # file name
    file_Name = "args.pickle"
    # open the file for writing
    fileObject = open(file_Name,'wb') 

    # this writes the object a to the
    # file named 'args.pickle'
    pickle.dump(args,fileObject)   

    # here we close the fileObject
    fileObject.close()
    # we open the file for reading
    #fileObject = open(file_Name,'r')  
    # load the object from the file into var b
    #b = pickle.load(fileObject)  

