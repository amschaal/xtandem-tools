import os
import glob
import argparse
import subprocess

def generate_scaffold_file(input_files,fasta_path,output_file,template,sample_template):
	driver_xml = open(output_file,'w')

	samples = '\n'.join([sample_template % {'input_file':input_file} for input_file in input_files])
#	if taxonomy_file_path:
#		extra += '<note type="input" label="list path, taxonomy information">%s</note>' % taxonomy_file_path 
	
	subs = {'fasta': fasta_path,
			'biological_samples':samples
			}
	
	driver_xml.write(template % subs)
	driver_xml.close()
	return output_file

def run(options):
	fasta_path = options.fasta_file
	output_file = options.output_file
	input_files = options.input_files
	template = open(options.template,'r').read()
	sample_template = open(options.sample_template,'r').read()
	generate_scaffold_file(input_files,fasta_path,output_file,template,sample_template)

def main():
	parser = argparse.ArgumentParser(description='Generate scaffold driver file based on a template, fasta file, and a list of input files.')
	parser.add_argument('--input_files', required=True, nargs='+', help='A file path to input files.  May use wildcards to use multiple files, such as *.mzml')
	parser.add_argument('--template', required=False, default='template.xml', help='The path to the default xml file.')
	parser.add_argument('--sample_template', required=False, default='sample_template.xml', help='The path to the default sample xml file.')
	parser.add_argument('--fasta_file', required=True, help='Fasta file')
	parser.add_argument('--output_file', required=True, help='The name/path of the driver file to be created.')
	options = parser.parse_args()
	run(options)

    #sys.stdout.flush()
    


if __name__ == '__main__':
	main()
    
