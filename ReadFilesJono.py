class ReadFilesJono():
    """Labai kieta klasė"""
    def __init__(self, file):
        file_content = open(file, mode='r', encoding='utf-8').readlines()
        self.U = [float(eilute.split(';')[0]) for eilute in file_content[1:]]
        self.I = []
        for eilute in file_content[1:]:
            try:
                self.I.append(float(eilute.split(';')[1]))
            except:
                self.I.append(float(0))
        self.j = [float(eilute.split(';')[2]) for eilute in file_content[1:]]
        self.P = [float(eilute.split(';')[3].strip()) for eilute in file_content[1:]]
        self.max_P = max(self.P)
        self.pce = f'{self.max_P/1000*100}%' 
        self.U_when_j_zero = [U for U, j in zip(self.U, self.j) if round(j, 0) == 0]
        self.j_when_U_zero = [j for U, j in zip(self.U, self.j) if round(U, 0) == 0]