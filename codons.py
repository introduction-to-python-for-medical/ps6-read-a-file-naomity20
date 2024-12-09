def create_codon_dict(file_path):
    file = open(path)
    rows = file.readlines()
    file.close()
    codons_dict = {}
    for row in rows:
      row_cells = row.strip().split('\t')
      codons_dict[row_cells[0]] = row_cells[2]
    return(codons_dict)


