from PIL import Image
import os
import glob
import cv2


def main():
    for d,d,filenames in os.walk("training_set_visible"):
        for filename in filenames:
#     '''
#     for infile in glob.glob("d_big_plate"):
#         file, ext = os.path.splitext(infile)
#         a,filename =os.path.split(file)
#     '''
#     col_name = args.input
            print "Start set input and output"
            print filename
        #     input_path = os.path.join(PIC_DIR, col_name + EXTENSION)
            
            input_path = "training_set_visible/"+filename
            img=Image.open(input_path)
            print img.getpixel((img.size[0]-1,img.size[1]-1))

            img = cv2.imread(input_path,cv2.IMREAD_UNCHANGED)
            file=open(input_path)
            file.__doc__
        #     output_path = os.path.join(PIC_DIR, col_name + '_bw' + EXTENSION)
#             img=cv2.resize(img,(28,28),interpolation = cv2.INTER_AREA)
            img=cv2.resize(img,(28,28),interpolation = cv2.INTER_NEAREST)
        
            output_path = "training_set_visible_28x28/"+filename
    
            print "input and output set over"
#             img.save(output_path)
            cv2.imwrite(output_path,img)
            
            print('Color picture saved to', output_path)
            img=Image.open(input_path)
            print img.getcolors()
            print len(img.getcolors())
            print img.getpixel((img.size[0]-1,img.size[1]-1))
if __name__ == '__main__':
#     sys.exit(main(sys.argv[1:]))
#     main(sys.argv[1:])
    main()
    print 'Done'