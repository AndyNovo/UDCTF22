import music21
s = music21.converter.parse('yoursonghere.mxl')

isBass = False #If pitches are too high or too low I just replace them with the min/max minecraft plays, setting True shifts the active octaves
ticksPerQN = 5 #minecraft ticks go 20 per second, so set how many 20ths of a second per Quarter Note
#I could totally switch instruments when the octaves are too high/low etc, but didn't
#Also I'm not doing any... repeating of parts of the sheet music.

notes=[]
for tN in s.recurse().getElementsByClass(['Note','Rest']):
    if (tN.name == 'rest'):
        notes.append([tN.name,tN.duration.quarterLength,tN.offset])
    else:
        notes.append([tN.pitch.frequency,tN.duration.quarterLength,tN.nameWithOctave])


mcfs=[round(pow(2,i/12.),3) for i in range(-12,13)]
therange = ['F#4', 'G4', 'G#4', 'A4', 'A#4', 'B4', 'C5', 'C#5', 'D5', 'D#5', 'E5', 'F5', 'F#5', 'G5', 'G#5', 'A5', 'A#5', 'B5', 'C6', 'C#6', 'D6', 'D#6', 'E6', 'F6', 'F#6']
if isBass:
    for i in range(len(therange)):
        therange[i] = therange[i].replace('4','2').replace('5','3').replace('6','4')

freqs=[music21.note.Note(x).pitch.frequency for x in therange]

def matchFreq(nf):
    for i in range(len(freqs)):
        if freqs[i] > nf:
            return mcfs[i]
    return mcfs[24]


res=[]
for note in notes:
    if note[0] == 'rest':
        res.append('x')
    else:
        res.append('"playsound block.note_block.iron_xylophone ambient @a ~ ~ ~ 5 %s"' % (matchFreq(note[0])))
    res += ['"x"' for _ in range(int(note[1]*ticksPerQN - 1))]

chunks = []
running = 0
temp = []
for page in res:
    running += len(page)
    temp.append(page)
    if running > 30000:
        chunks.append(temp)
        running = 0
        temp = []
chunks.append(temp)

for chunk in chunks:
    cmd = '/give @p minecraft:writable_book{pages:[%s]}' % (",".join(chunk))
    print(cmd)
