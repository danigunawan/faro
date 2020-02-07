'''
Created on Dec 3, 2019 at Oak Ridge National Laboratory

@author: qdb
'''
import sys
import optparse
import os

import faro
import pyvision as pv
import cv2
import faro.proto.proto_types as pt


def addConnectionOptions(parser):
    ''' Add options for connecting to the faro service. '''
    
    connection_group = optparse.OptionGroup(parser, "Connection Options",
                        "Control the connection to the FaRO service.")
    
    connection_group.add_option( "--max-async", type="int", dest="max_async", default=faro.DEFAULT_MAX_ASYNC,
                      help="The maximum number of asyncronous call to make at a time. Default=%d"%faro.DEFAULT_MAX_ASYNC)

    connection_group.add_option( "--max-message-size", type="int", dest="max_message_size", default=faro.DEFAULT_MAX_MESSAGE_SIZE,
                      help="Maximum GRPC message size. Set to -1 for unlimited. Default=%d"%(faro.DEFAULT_MAX_MESSAGE_SIZE))

    connection_group.add_option( "-p", "--port", type="str", dest="detect_port", default="localhost:50030",
                      help="The port used for the recognition service.")

    connection_group.add_option( "--detect-port", type="str", dest="detect_port", default="localhost:50030",
                      help="The port used for the recognition service.")

    connection_group.add_option( "--recognition-port", type="str", dest="rec_port", default="localhost:50030",
                      help="The port used for the recognition service.")
    
    parser.add_option_group(connection_group)




def addDetectorOptions(parser):
    ''' Add options for detections to the parser. '''
    
    detector_group = optparse.OptionGroup(parser, "Detector Options",
                        "Configuration for the face detector.")

    detector_group.add_option( "-d","--detections-csv", type="str", dest="detections_csv", default=None,
                      help="Save detection data to the file.")

    detector_group.add_option( "-a","--attributes-csv", type="str", dest="attributes_csv", default=None,
                      help="Save attributes data to the file.")

    detector_group.add_option( "--detect-log", type="str", dest="detect_log", default=None,
                      help="A directory for detection images.")

    detector_group.add_option( "--face-log", type="str", dest="face_log", default=None,
                      help="A directory for faces.")

    detector_group.add_option("-b", "--best", action="store_true", dest="best", default=False,
                      help="Detect the 'best' highest scoring face in the image.")
    
    detector_group.add_option( "--detect-thresh", type="float", dest="detect_thresh", default=None,
                      help="The threshold for a detection.")

    detector_group.add_option( "--min-size", type="int", dest="min_size", default=64,
                      help="Faces with a height less that this will be ignored.")
    
    detector_group.add_option( "--attribute-filter", type="str", dest="attribute_filter", default=None,
                      help="A comma seperated list of filters example: 'Male>0.5'" )
    
    parser.add_option_group(detector_group)
    
    
def addEnrollOptions(parser):
    ''' Add options for enrollment into a gallery. '''
    
    enroll_group =  optparse.OptionGroup(parser, "Enrollment Options",
                        "Configuration for enrollment.")
    #parser.add_option( "--enroll", type="str", dest="enroll_gallery", default=None,
    #                   help="Enroll detected faces into a gallery.")
    
    enroll_group.add_option( "-e", "--enroll-csv", type="str", dest="enroll_csv", default='default',
                       help="Save a log of the enrollments.")
    
    enroll_group.add_option( "--enroll-gallery", type="str", dest="enroll_gallery", default='default',
                       help="Select the gallery to enroll into.")
    
    enroll_group.add_option( "--name", type="str", dest="subject_name", default='UNKNOWN',
                       help="Enroll detected faces into a gallery.")
    
    enroll_group.add_option( "--subject-id", type="str", dest="subject_id", default='unknown',
                       help="Enroll detected faces into a gallery.")
    
    parser.add_option_group(enroll_group)


def addSearchOptions(parser):
    ''' Add options for enrollment into a gallery. '''
    
    enroll_group =  optparse.OptionGroup(parser, "Enrollment Options",
                        "Configuration for enrollment.")

    enroll_group.add_option( "-s", "--search-csv", type="str", dest="search_csv", default='default',
                       help="Save the search results.")
    
    enroll_group.add_option( "--search-gallery", type="str", dest="search_gallery", default='default',
                       help="Select the gallery to search.")
        
    parser.add_option_group(enroll_group)



def preprocessImage(im,options):
    
    # Reduce the size if the image is too large
    scale = 1.0
    while max(*im.shape[:2]) > options.max_size:
        if max(*im.shape[:2]) > 2*options.max_size:
            im = cv2.pyrDown(im)
            scale *= 0.5
        else:
            w,h = im.shape[:2]
            s = options.max_size/max(w,h)
            scale *= s
            w = int(s*w)
            h = int(s*h)
            im = cv2.resize(im,(w,h))
    return im


def detectParseOptions():
    '''
    Parse command line arguments.
    '''
    args = ['[image] [image_directory] [video] [...]'] # Add the names of arguments here.
    n_args = len(args)
    args = " ".join(args)
    description = '''Run detection on a collection of images.'''
    epilog = '''Created by David Bolme - bolmeds@ornl.gov'''
    
    version = faro.__version__
    
    
    # Setup the parser
    parser = optparse.OptionParser(usage='%s command [OPTIONS] %s'%(sys.argv[0],args),version=version,description=description,epilog=epilog)

    parser.add_option( "-v", "--verbose", action="store_true", dest="verbose", default=False,
                      help="Print out more program information.")
    
    parser.add_option( "-n","--max-images", type="int", dest="max_images", default=None,
                      help="Process at N images and then stop.")

    parser.add_option( "--maximum-size", type="int", dest="max_size", default=faro.DEFAULT_MAX_SIZE,
                      help="If too large, images will be scaled to have this maximum size. Default=%d"%(faro.DEFAULT_MAX_SIZE))
    
    addDetectorOptions(parser)
    addConnectionOptions(parser)
    # Here are some templates for standard option formats.
    #parser.add_option("-q", "--quiet", action="store_false", dest="verbose", default=True,
    #                 help="Decrease the verbosity of the program")

    #parser.add_option("-b", "--bool", action="store_true", dest="my_bool", default=False,
    #                  help="don't print status messages to stdout")
    
    #parser.add_option( "-c","--choice", type="choice", choices=['c1','c2','c3'], dest="my_choice", default="c1",
    #                  help="Choose an option.")

    #parser.add_option( "-f","--float", type="float", dest="my_float", default=0.0,
    #                  help="A floating point value.")

    #parser.add_option( "-i","--int", type="int", dest="my_int", default=0,
    #                  help="An integer value.")

    #parser.add_option( "-s","--str", type="str", dest="my_str", default="default",
    #                  help="A string value.")

    #parser.add_option( "--enroll", type="str", dest="enroll_gallery", default=None,
    #                  help="Enroll detected faces into a gallery.")
    
    #parser.add_option( "--search", type="str", dest="search_gallery", default=None,
    #                  help="Search images for faces from a gallery.")
    
    #parser.add_option( "--name", type="str", dest="subject_name", default=None,
    #                  help="Enroll detected faces into a gallery.")
    
    #parser.add_option( "--subject-id", type="str", dest="subject_id", default=None,
    #                  help="Enroll detected faces into a gallery.")
    
    #parser.add_option( "--search-log", type="str", dest="search_log", default=None,
    #                  help="Enroll detected faces into a gallery.")
    
    #parser.add_option( "-m","--match-log", type="str", dest="match_log", default=None,
    #                  help="A directory to store matching faces.")

    #parser.add_option( "--same-person", type="str", dest="same_person", default=None,
    #                  help="Specifies a python function that returns true if the filenames indicate a match.  Example: lambda x,y: x[:5] == y[:5]")

    #parser.add_option( "-s","--scores-csv", type="str", dest="scores_csv", default=None,
    #                  help="Save similarity scores to this file.")


    # Parse the arguments and return the results.
    (options, args) = parser.parse_args()
    
    if len(args) < 1:
        parser.print_help()
        print()
        print(( "Please supply exactly %d arguments."%n_args ))
        print()
        exit(-1)
        
    return options,args


def enrollParseOptions():
    '''
    Parse command line arguments.
    '''
    args = ['[image] [image_directory] [video] [...]'] # Add the names of arguments here.
    n_args = len(args)
    args = " ".join(args)
    description = '''Run detection on a collection of images.'''
    epilog = '''Created by David Bolme - bolmeds@ornl.gov'''
    
    version = faro.__version__
    
    
    
    # Setup the parser
    parser = optparse.OptionParser(usage='%s command [OPTIONS] %s'%(sys.argv[0],args),version=version,description=description,epilog=epilog)

    parser.add_option( "-v", "--verbose", action="store_true", dest="verbose", default=False,
                      help="Print out more program information.")
    
    parser.add_option( "-n","--max-images", type="int", dest="max_images", default=None,
                      help="Process at N images and then stop.")

    parser.add_option( "--maximum-size", type="int", dest="max_size", default=faro.DEFAULT_MAX_SIZE,
                      help="If too large, images will be scaled to have this maximum size. Default=%d"%(faro.DEFAULT_MAX_SIZE))
    
    addEnrollOptions(parser)
    addDetectorOptions(parser)
    addConnectionOptions(parser)

    # Parse the arguments and return the results.
    (options, args) = parser.parse_args()
    
    if len(args) < 2:
        parser.print_help()
        print()
        print(( "Error: Please supply at least one directory, image, or video."))
        print()
        exit(-1)
        
        
    return options,args

def searchParseOptions():
    '''
    Parse command line arguments.
    '''
    args = ['[image] [image_directory] [video] [...]'] # Add the names of arguments here.
    n_args = len(args)
    args = " ".join(args)
    description = '''Run detection on a collection of images.'''
    epilog = '''Created by David Bolme - bolmeds@ornl.gov'''
    
    version = faro.__version__
    
    
    
    # Setup the parser
    parser = optparse.OptionParser(usage='%s command [OPTIONS] %s'%(sys.argv[0],args),version=version,description=description,epilog=epilog)

    parser.add_option( "-v", "--verbose", action="store_true", dest="verbose", default=False,
                      help="Print out more program information.")
    
    parser.add_option( "-n","--max-images", type="int", dest="max_images", default=None,
                      help="Process at N images and then stop.")

    parser.add_option( "--maximum-size", type="int", dest="max_size", default=faro.DEFAULT_MAX_SIZE,
                      help="If too large, images will be scaled to have this maximum size. Default=%d"%(faro.DEFAULT_MAX_SIZE))
    
    addSearchOptions(parser)
    addDetectorOptions(parser)
    addConnectionOptions(parser)

    # Parse the arguments and return the results.
    (options, args) = parser.parse_args()
    
    if len(args) < 2:
        parser.print_help()
        print()
        print(( "Error: Please supply at least one directory, image, or video."))
        print()
        exit(-1)
        
        
    return options,args


def connectToFaroClient(options):
    if options.verbose:
        print('Connecting to FaRO Service...')

    face_client = faro.FaceClient(options)
    
    is_ready,status = face_client.status(verbose=options.verbose)
    if not is_ready:
        print("ERROR: the FaRO service is not ready.")
        print(status)
        exit(-1)
    else:
        if options.verbose:
            print('Connection to FaRO service established. [ algorithm: %s ]'%(status.algorithm))
    
    return face_client


def collect_files(args,options):
    if options.verbose:
        print('Scanning for videos and images...')

    image_list = []
    video_list = []
    
    for each in args:
        if os.path.isdir(each):
            for path,dirs,files in os.walk(each):
                for filename in files:
                    if pv.isImage(filename):
                        image_list.append(os.path.join(path,filename))
                    elif pv.isVideo(filename):
                        video_list.append(os.path.join(path,filename))
                    
        elif os.path.isfile(each): 
            if pv.isImage(each):
                image_list.append(each)
            elif pv.isVideo(each):
                video_list.append(each)
            else:
                raise ValueError("The file <%s> is not in a supported image or video type."%(each))
        else:
            raise ValueError("The path <%s> is not found."%(each))
        
    if options.verbose:
        print("    Found %d images."%(len(image_list)))
        print("    Found %d videos."%(len(video_list)))
        
    return image_list, video_list


def processAttributeFilter(face,options):
    if options.attribute_filter is None:
        return True
    
    # Parse the filter
    terms = options.attribute_filter.split(',')
    new_terms = []
    for each in terms:
        try:
            parts = each.split('>')
            parts = parts[0], '>', float(parts[1])
            assert len(parts) == 3
        except:
            try:
                parts = each.split('<')
                print (parts)
                parts = parts[0], '<', float(parts[1])
                assert len(parts) == 3
            except:
                raise ValueError("Could not parse term '%s'."%each)
            
        new_terms.append(parts)
            
    satisfied = 0

    attributes = list(face.attributes)
    attributes.sort(key=lambda x: x.key)

    for attribute in attributes:
        key = attribute.key
        value = attribute.fvalue
        for tkey,tcmp,tval in new_terms:
            if tkey == key and value > tval and tcmp == '>':
                satisfied += 1
            if tkey == key and value < tval and tcmp == '<':
                satisfied += 1
                
    #assert satisfied <= len(terms) # Make sure we get an expected answer
    
    return satisfied == len(terms)
           
    
        
          
DETECTIONS_FILE = None  
DETECTIONS_CSV = None  
ATTRIBUTES_FILE = None  
ATTRIBUTES_CSV = None    

def processDetections(each):
    im, results, options = each
    if results.done():
        recs = results.result().face_records
        i = 0


        for face in recs:
            # Filter faces based on min size
            size = min(face.detection.location.width,face.detection.location.height)
            if size < options.min_size:
                continue
            
            # Filter faces based on attributes
            if not processAttributeFilter(face,options):
                continue
            
            # Process Detections
            if options.detections_csv is not None:
                global DETECTIONS_CSV
                global DETECTIONS_FILE
                import csv 
                if DETECTIONS_CSV == None:
                    DETECTIONS_FILE = open(options.detections_csv,'w')
                    DETECTIONS_CSV = csv.writer(DETECTIONS_FILE)
                    DETECTIONS_CSV.writerow(['source','frame','detect_id','type','score','x','y','w','h']) 
                    
                DETECTIONS_CSV.writerow([face.source,
                                        face.frame,
                                        i,
                                        face.detection.detection_class,
                                        face.detection.score,
                                        face.detection.location.x,
                                        face.detection.location.y,
                                        face.detection.location.width,
                                        face.detection.location.height
                                        ]),
                DETECTIONS_FILE.flush()
                
            # Process Detections
            if options.attributes_csv is not None:
                global ATTRIBUTES_CSV
                global ATTRIBUTES_FILE
                import csv 
                
                if ATTRIBUTES_CSV == None:
                    ATTRIBUTES_FILE = open(options.attributes_csv,'w')
                    ATTRIBUTES_CSV = csv.writer(ATTRIBUTES_FILE)
                    ATTRIBUTES_CSV.writerow(['source','frame','detect_id','type','score','x','y','w','h','attribute','value']) 
                    
                attributes = list(face.attributes)
                attributes.sort(key=lambda x: x.key)
                for attribute in attributes:
                    key = attribute.key
                    value = attribute.fvalue
                    ATTRIBUTES_CSV.writerow([face.source,
                                            face.frame,
                                            i,
                                            face.detection.detection_class,
                                            face.detection.score,
                                            face.detection.location.x,
                                            face.detection.location.y,
                                            face.detection.location.width,
                                            face.detection.location.height,
                                            key,
                                            value,
                                            ]),
                ATTRIBUTES_FILE.flush()
                
                # Save Images with Detections
            
                
                # Save Detected Faces
                face_out_dir = ""    
            
            if options.face_log:
                if not os.path.exists(options.face_log):
                    os.makedirs(options.face_log, exist_ok=True)
                #print(face.detection.location)
                
                rect = pt.rect_proto2pv(face.detection.location)
                rect = rect.rescale(1.5)
                affine = pv.AffineFromRect(rect,(128,128))
                try:
                    pvim = pv.Image(im[:,:,::-1])
                    view = affine(pvim)
                    #print('Face',rect)
                    #print(view)
                    base_name,ext = os.path.splitext(os.path.basename(face.source))
                    out_path = os.path.join(options.face_log,os.path.basename(base_name)+'_face_%03d'%(face.detection.detection_id,)+ext)
                    
                    view.save(out_path)
                    print('Saving face:',out_path)
                except:
                    print("WARNING: Image not processed correctly:",face.source)
                    
                out_path = os.path.join(options.face_log,os.path.basename(base_name)+'_orig'+ext)
        
                if not os.path.lexists(out_path):
                    os.symlink(os.path.abspath(face.source),out_path)
                
                
                #print(options.face_log)
                #pass
            i += 1
        

        return False
    return True

ENROLL_FILE = None  
ENROLL_CSV = None  

def processEnrollments(each):
    im, results, options = each
    
    if results.done():
        recs = results.result().face_records
        i = 0
        for face in recs:
            # Filter faces based on min size
            size = min(face.detection.location.width,face.detection.location.height)
            if size < options.min_size:
                continue
            
            # Filter faces based on attributes
            if not processAttributeFilter(face,options):
                continue
            
            # Process Detections
            if options.enroll_csv is not None:
                global ENROLL_CSV
                global ENROLL_FILE
                import csv 
                if ENROLL_CSV == None:
                    ENROLL_FILE = open(options.enroll_csv,'w')
                    ENROLL_CSV = csv.writer(ENROLL_FILE)
                    ENROLL_CSV.writerow(['gallery_key','source','frame','detect_id','type','score','x','y','w','h']) 
                    
                ENROLL_CSV.writerow([face.gallery_key,face.source,
                                        face.frame,
                                        i,
                                        face.detection.detection_class,
                                        face.detection.score,
                                        face.detection.location.x,
                                        face.detection.location.y,
                                        face.detection.location.width,
                                        face.detection.location.height
                                        ]),
                ENROLL_FILE.flush()
                
            i += 1
        return False
    return True

SEARCH_CSV = None
SEARCH_FILE = None
def processSearchResults(each):
    print('Search results')
    im, results, options = each
    
    if results.done():
        print('Done')
        recs = results.result().face_records
        print(recs)
        i = 0
        for face in recs:
            # Filter faces based on min size
            size = min(face.detection.location.width,face.detection.location.height)
            if size < options.min_size:
                continue
            
            # Filter faces based on attributes
            if not processAttributeFilter(face,options):
                continue
            
            # Process Detections
            print( "Face" )
            if options.search_csv is not None:
                global SEARCH_CSV
                global SEARCH_FILE
                import csv 
                if SEARCH_CSV == None:
                    SEARCH_FILE = open(options.search_csv,'w')
                    SEARCH_CSV = csv.writer(SEARCH_FILE)
                    SEARCH_CSV.writerow(['gallery_key','source','frame','detect_id','type','score','x','y','w','h']) 
                    
                SEARCH_CSV.writerow([face.gallery_key,face.source,
                                        face.frame,
                                        i,
                                        face.detection.detection_class,
                                        face.detection.score,
                                        face.detection.location.x,
                                        face.detection.location.y,
                                        face.detection.location.width,
                                        face.detection.location.height
                                        ]),
                SEARCH_FILE.flush()
                
            i += 1
        return False
    return True


def detect():
    options,args = detectParseOptions()
    face_client = connectToFaroClient(options)

    if options.verbose:
        print("Scanning directories for images and videos.")
    
    image_list, video_list = collect_files(args[1:],options)

    if options.verbose:
        print("Processing images.")
        
    image_count = 0
    detect_queue = []
    
    for filename in image_list:
        print("Processing:",filename)
        im = cv2.imread(filename)
        im = im[:,:,::-1] # BGR to RGB
        
        im = preprocessImage(im, options)
        
        results = face_client.detectExtract(im, best = options.best, threshold=options.detect_thresh, min_size=options.min_size, run_async=True, source=filename, frame=-1)
        
        detect_queue.append([im,results,options])
        detect_queue = list(filter(processDetections,detect_queue))
        
        image_count += 1
        if options.max_images is not None and image_count >= options.max_images:
            break
        
    import time
                    
    while len(detect_queue):
        detect_queue = list(filter(processDetections,detect_queue))
        time.sleep(0.05)
        
    if len(video_list) > 0:
        print("WARNING: Video Processing Is Not Implemented. %d videos skipped."%(video_list,))

    
    
    
def enroll():
    options,args = enrollParseOptions()
    face_client = connectToFaroClient(options)

    if options.verbose:
        print("Scanning directories for images and videos.")
    
    image_list, video_list = collect_files(args[1:],options)

    if options.verbose:
        print("Processing images.")
        
    image_count = 0
    detect_queue = []
    enroll_queue = []
    
    for filename in image_list:
        print("Processing:",filename)
        im = cv2.imread(filename)
        im = im[:,:,::-1] # BGR to RGB
        
        im = preprocessImage(im, options)
        
        results = face_client.detectExtractEnroll(im, enroll_gallery=options.enroll_gallery, best = options.best, threshold=options.detect_thresh, min_size=options.min_size, run_async=True, source=filename, frame=-1)
        
        detect_queue.append([im,results,options])
        enroll_queue.append([im,results,options])

        # Process results that are completed.
        detect_queue = list(filter(processDetections,detect_queue))
        enroll_queue = list(filter(processEnrollments,enroll_queue))
        
        image_count += 1
        if options.max_images is not None and image_count >= options.max_images:
            break
        
    import time
                    
    # Finish processing.
    while len(detect_queue):
        detect_queue = list(filter(processDetections,detect_queue))
        time.sleep(0.05)

    while len(enroll_queue):
        enroll_queue = list(filter(processEnrollments,enroll_queue))
        time.sleep(0.05)

    if len(video_list) > 0:
        print("WARNING: Video Processing Is Not Implemented. %d videos skipped."%(video_list,))



def search():
    options,args = searchParseOptions()
    face_client = connectToFaroClient(options)

    if options.verbose:
        print("Scanning directories for images and videos.")
    
    image_list, video_list = collect_files(args[1:],options)

    if options.verbose:
        print("Processing images.")
        
    image_count = 0
    detect_queue = []
    search_queue = []
    
    for filename in image_list:
        print("Processing:",filename)
        im = cv2.imread(filename)
        im = im[:,:,::-1] # BGR to RGB
        
        im = preprocessImage(im, options)
        
        results = face_client.detectExtractSearch(im, search_gallery=options.search_gallery, best = options.best, threshold=options.detect_thresh, min_size=options.min_size, run_async=True, source=filename, frame=-1)
        
        detect_queue.append([im,results,options])
        search_queue.append([im,results,options])

        # Process results that are completed.
        detect_queue = list(filter(processDetections,detect_queue))
        search_queue = list(filter(processSearchResults,search_queue))
        
        image_count += 1
        if options.max_images is not None and image_count >= options.max_images:
            break
        
    import time
                    
    # Finish processing.
    while len(detect_queue):
        detect_queue = list(filter(processDetections,detect_queue))
        time.sleep(0.05)

    while len(search_queue):
        search_queue = list(filter(processSearchResults,search_queue))
        time.sleep(0.05)

    if len(video_list) > 0:
        print("WARNING: Video Processing Is Not Implemented. %d videos skipped."%(video_list,))



COMMANDS = {
    'detect' : ['Only run face detection and attribute extraction.',detect],
    'enroll' : ['Extract faces and enroll faces in a gallery.',enroll],
    'search' : ['Search images for faces in a gallery.',search],
            }
    

def face_command_line():
    if len(sys.argv) < 2 or sys.argv[1] not in COMMANDS:
        # Display a basic help message if no command is specified
        print()
        print("ERROR: You must a command command.  For more help run %s <command> --help.\n\nCommands:"%(sys.argv[0]))
        for each in COMMANDS:
            print("    %s - %s"%(each,COMMANDS[each][0]))
        print()
        exit(-1)
        
    # Jump to the entry point for the command.
    COMMANDS[sys.argv[1]][1]()
        
        
            
    
if __name__ == '__main__':
    face_command_line()