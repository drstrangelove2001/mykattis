T = int(input())
for _ in range(T):
    voices = dict()
    recording = input()
    ans = []
    while True:
        voice = input()
        if voice == 'what does the fox say?':
            for rec in recording.split():
                if rec not in voices:
                    ans.append(rec)
            print(' '.join(ans))
            break
        else:
            voices[voice.split()[2]] = voice.split()[0]