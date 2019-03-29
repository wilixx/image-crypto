from PIL import Image
import os
import glob

def main():
    for d,d,filenames in os.walk("training_data_7000_0_16base_visible"):
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
            
            input_path = "training_data_7000_0_16base_visible/"+filename
            img=Image.open(input_path).convert('LA')
            file=open(input_path)
            file.__doc__
        #     output_path = os.path.join(PIC_DIR, col_name + '_bw' + EXTENSION)
        
        
            output_path = "training_data_7000_0_16base_visible_gray/"+filename
    
            print "input and output set over"
            img.save(output_path)
            print('Color picture saved to', output_path)

if __name__ == '__main__':
#     sys.exit(main(sys.argv[1:]))
#     main(sys.argv[1:])
    main()
    print 'Done'