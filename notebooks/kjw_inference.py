import logging
import os


def find_iter(directory, start, stop):
    logging.debug("Finding iteration files for {} in [{},{}]".format(directory, start, stop))
    files = [ i for i in os.listdir(directory) if i.endswith('caffemodel.h5')]
    ret=[]
    for _file in files:
        iter_num=int(_file.split('_')[-1].split('.')[0])
        if iter_num>=start and iter_num<=stop:
            ret.append(os.path.join(directory,_file))
    logging.debug("Found: [{}] Entries".format(len(ret)))
    return ret

if __name__ == "__main__":
  from optparse import OptionParser
  logging.basicConfig(level=logging.DEBUG)
  logging.debug("Starting")
  usage = """usage: %prog [options] -m <model file directory> -p <prototext file>
"""
  parser = OptionParser(usage=usage)
  parser.add_option("-c", "--config", dest="config", default="testA.cfg",
                    help="Configuration (Usually testA.cfg or testB.cfg)", metavar="FILE")
  parser.add_option("-p", "--prototxt",
                  dest="proto",
                  help="Path to prototxt FILE")
  parser.add_option("-m", "--model-dir",
                  dest="model_dir",
                  default =None,
                  help="Path to DIRECTORY containing MODELS")
  parser.add_option("-s", "--start",
                  dest="start", default=0,
                  help="Starting model iteration for running inference")
  parser.add_option("-e", "--stop",
                  dest="stop", default=100000000,
                  help="Stopping model iteration for running inference")
  parser.add_option("-o", "--out",
                  dest="out", default='testA',
                  help="Output Directory")
  
  (options, args) = parser.parse_args() 
  if options.proto is None:
    parser.print_help()
  model_dir =  options.model_dir if  options.model_dir is not None else os.path.abspath(os.path.join(options.proto, '..'))

  iterations = find_iter(model_dir, int(options.start), int(options.stop))
  from inference import inference
  for _iter in iterations:
    logging.debug("Running Inference on snapshot: "+_iter)
    p = inference()
    output = os.path.join(options.out,_iter.split('/')[-1].replace('.caffemodel.h5','.csv'))
    logging.debug("Prototext: {}".format(options.proto))
    logging.debug("Weight: {}".format(_iter))
    logging.debug("Output: {}".format(output))
    logging.debug("IO Config: {}".format(options.config))
    p.configure(proto=options.proto,weight=_iter,output=output,io_cfg=options.config)
    p.run()
    os.chmod(output, 777)
    logging.debug("Done.")
