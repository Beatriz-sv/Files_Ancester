from modeller import *

env = environ()
aln = alignment(env)
mdl = model(env, file='5i3d', model_segment=('FIRST:C','LAST:C'))
aln.append_model(mdl, align_codes='5i3dC', atom_files='5i3d.pdb')
aln.append(file='target.fasta', align_codes='target', alignment_format='FASTA')
aln.align2d()
aln.write(file='aligned.fasta', alignment_format='FASTA')
aln.write(file='aligned.ali', alignment_format='PIR')
aln.write(file='aligned.pap', alignment_format='PAP')