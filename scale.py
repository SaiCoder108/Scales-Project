    # Project to Convert Swarams + Scale to listable Scale
def process_swarams(scale, chord):
    # Constants
    rank = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#","A", "A#", "B"]
    swarams = ["S","R1","R2","G1","G2","M1","M2","P","D1","D2","N1","N2"]

    # Convert Chord to Notes
    for y in range(len(chord)):
        chord[y] = swarams.index(chord[y])

    # Shift Postion of Chord to Scale
    factor = rank.index(scale)
    for y in range(len(chord)):
        if chord[y] + factor > 11:
            chord[y] = (chord[y]+factor)-12
        else: 
            chord[y] += factor

    # Convert back to Notes
    sc_chord = []
    for z in range(len(chord)):
        sc_chord.append(rank[chord[z]])

    # Convert Back into Swarams on new scale
    sc_swarams = []
    for x in range(len(sc_chord)):
        temp = (rank.index(sc_chord[x]) - rank.index(sc_chord[0])) % 12
        sc_swarams.append(swarams[temp])

    sc_swarams = ", ".join(sc_swarams)

    return (f"The chord to play realtive to C scale is: {sc_swarams} on the scale {sc_chord[0]}")

