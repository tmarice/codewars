
translation_table = str.maketrans({
    'A': 'T',
    'T': 'A',
    'G': 'C',
    'C': 'G',
})

def DNA_strand(s):
    return s.translate(translation_table)
