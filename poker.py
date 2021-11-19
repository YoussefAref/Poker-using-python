def compare_hands(hand1,hand2):
    hand1=list(hand1)
    hand2=list(hand2)
    for i in hand1:
        if i=='A S' or i=='A D' or i=='A H' or i=='A C':
            l=hand1.index(i)
            i='>'+' '+i[2]
            hand1[l]=i
    for i in hand2:
        if i=='A S' or i=='A D' or i=='A H' or i=='A C':
            l=hand2.index(i)
            i='>'+' '+i[2]
            hand2[l]=i
    for i in hand1:
        if i=='K S' or i=='K D' or i=='K H' or i=='K C':
            l=hand1.index(i)
            i='='+' '+i[2]
            hand1[l]=i
    for i in hand2:
        if i=='K S' or i=='K D' or i=='K H' or i=='K C':
            l=hand2.index(i)
            i='='+' '+i[2]
            hand2[l]=i
    for i in hand1:
        if i=='Q S' or i=='Q D' or i=='Q H' or i=='Q C':
            l=hand1.index(i)
            i='<'+' '+i[2]
            hand1[l]=i
    for i in hand2:
        if i=='Q S' or i=='Q D' or i=='Q H' or i=='Q C':
            l=hand2.index(i)
            i='<'+' '+i[2]
            hand2[l]=i
    for i in hand1:
        if i=='J S' or i=='J D' or i=='J H' or i=='J C':
            l=hand1.index(i)
            i=';'+' '+i[2]
            hand1[l]=i
    for i in hand2:
        if i=='J S' or i=='J D' or i=='J H' or i=='J C':
            l=hand2.index(i)
            i=';'+' '+i[2]
            hand2[l]=i
    for i in hand1:
        if i=='10 S' or i=='10 D' or i=='10 H' or i=='10 C':
            l=hand1.index(i)
            i=':'+' '+i[3]
            hand1[l]=i
    for i in hand2:
        if i=='10 S' or i=='10 D' or i=='10 H' or i=='10 C':
            l=hand2.index(i)
            i=':'+' '+i[3]
            hand2[l]=i
    hand1=sorted((hand1), reverse=True)
    hand2=sorted((hand2), reverse=True)
    score1=0
    score2=0
    if (hand1[0][2]==hand1[1][2]==hand1[2][2]==hand1[3][2]==hand1[4][2]):
        i=0
        SF1=0
        while int(ord(hand1[i][0]))-int(ord(hand1[i+1][0]))==1:
            SF1+=1
            i+=1
            if SF1==4:
                score1=9
                break
    if (hand2[0][2]==hand2[1][2]==hand2[2][2]==hand2[3][2]==hand2[4][2]):
        i=0
        SF2=0
        while int(ord(hand2[i][0]))-int(ord(hand2[i+1][0]))==1:
            SF2+=1
            i+=1
            if SF2==4:
                score2=9
                break
    if score1==score2!=0:
        if hand1[0][0]>hand2[0][0]:
            return(1)
        elif hand1[0][0]<hand2[0][0]:
            return(-1)
        else:
            return(0)
    if (hand1[0][0]==hand1[1][0]==hand1[2][0]==hand1[3][0]) or (hand1[1][0]==hand1[2][0]==hand1[3][0]==hand1[4][0]) and score1==0:
        score1=8
    if (hand2[0][0]==hand2[1][0]==hand2[2][0]==hand2[3][0]) or (hand2[1][0]==hand2[2][0]==hand2[3][0]==hand2[4][0]) and score2==0:
        score2=8
    if score1==score2!=0:
        if hand1[1][0]>hand2[1][0]:
            return(1)
        elif hand1[1][0]<hand2[1][0]:
            return(-1)
        else:
            return(0)
    if (hand1[0][0]==hand1[1][0]==hand1[2][0] and hand1[3][0]==hand1[4][0]) or (hand1[0][0]==hand1[1][0] and hand1[2][0]==hand1[3][0]==hand1[4][0]) and score1==0:
        score1=7
    if (hand2[0][0]==hand2[1][0]==hand2[2][0] and hand2[3][0]==hand2[4][0]) or (hand2[0][0]==hand2[1][0] and hand2[2][0]==hand2[3][0]==hand2[4][0]) and score2==0:
        score2=7
    if score1==score2!=0:
        if hand1[2][0]>hand2[2][0]:
            return(1)
        elif hand1[2][0]<hand2[2][0]:
            return(-1)
        else:
            return(0)
    if (hand1[0][2]==hand1[1][2]==hand1[2][2]==hand1[3][2]==hand1[4][2]) and score1==0:
        score1=6
    if (hand2[0][2]==hand2[1][2]==hand2[2][2]==hand2[3][2]==hand2[4][2]) and score2==0:
        score2=6
    if score1==score2!=0:
        i=0
        while i<4 and (hand1[i][0]==hand2[i][0]):
            hand1[i][0]==hand2[i][0]
            i+=1
        if hand1[i][0]>hand2[i][0]:
            return(1)
        elif hand1[i][0]<hand2[i][0]:
            return(-1)
        else:
            return(0)
    if (int(ord(hand1[0][0]))-int(ord(hand1[1][0]))==1) and score1==0:
        i=0
        OB1=0
        while i<4 and(int(ord(hand1[i][0]))-int(ord(hand1[i+1][0]))==1):
            OB1+=1
            i+=1
            if OB1==4:
                score1=5
    if (int(ord(hand2[0][0]))-int(ord(hand2[1][0]))==1) and score2==0:
        i=0
        OB2=0
        while i<4 and ((int(ord(hand2[i][0])))-(int(ord(hand2[i+1][0])))==1):
            OB2+=1
            i+=1
            if OB2==4:
                score2=5
    if score1==score2!=0:
        if hand1[0][0]>hand2[0][0]:
            return(1)
        elif hand1[0][0]<hand2[0][0]:
            return(-1)
        else:
            return(0)
    if ((hand1[0][0]==hand1[1][0]==hand1[2][0]) or (hand1[1][0]==hand1[2][0]==hand1[3][0]) or (hand1[2][0]==hand1[3][0]==hand1[4][0])) and score1==0:
        score1=4
    if ((hand2[0][0]==hand2[1][0]==hand2[2][0]) or (hand2[1][0]==hand2[2][0]==hand2[3][0]) or (hand2[2][0]==hand2[3][0]==hand2[4][0])) and score2==0:
        score2=4
    if score1==score2!=0:
        if hand1[2][0]>hand2[2][0]:
            return(1)
        elif hand1[2][0]<hand2[2][0]:
            return(-1)
        else:
            return(0)
    if ((hand1[0][0]==hand1[1][0] and hand1[2][0]==hand1[3][0]) or (hand1[1][0]==hand1[2][0] and hand1[3][0]==hand1[4][0]) or (hand1[0][0]==hand1[1][0] and hand1[3][0]==hand1[4][0])) and score1==0:
        score1=3
    if ((hand2[0][0]==hand2[1][0] and hand2[2][0]==hand2[3][0]) or (hand2[1][0]==hand2[2][0] and hand2[3][0]==hand2[4][0]) or (hand2[0][0]==hand2[1][0] and hand2[3][0]==hand2[4][0])) and score2==0:
        score2=3
    if score1==score2!=0:
        i=0
        while (hand1[i][0]==hand2[i][0]) and i<4:
            i+=1
        if hand1[i][0]>hand2[i][0]:
            return(1)
        elif hand1[i][0]<hand2[i][0]:
            return(-1)
        else:
            return(0)
    else:
        if score1>score2:
            return(1)
        elif score1<score2:
            return(-1)
        else:
            return(0)
    if (hand1[0][0]==hand1[1][0] or hand1[1][0]==hand1[2][0] or hand1[2][0]==hand1[3][0] or hand1[3][0]==hand1[4][0]) and score1==0:
        score1=2
        if (hand1[0][0]==hand1[1][0] or hand1[1][0]==hand1[2][0]):
            i=1
        else:
            i=3
    if (hand2[0][0]==hand2[1][0] or hand2[1][0]==hand2[2][0] or hand2[2][0]==hand2[3][0] or hand2[3][0]==hand2[4][0]) and score2==0:
        score2=2
        if (hand2[0][0]==hand2[1][0] or hand2[1][0]==hand2[2][0]):
            j=1
        else:
            j=3
    if score1==score2!=0:
        if hand1[i][0]>hand2[j][0]:
            return(1)
        elif hand1[i][0]<hand2[j][0]:
            return(-1)
        else:
            return(0)
    if score1==score2==0:
        i=0
        while (hand1[i][0]==hand2[i][0]) and i<4:
            i+=1
        if hand1[i][0]>hand2[i][0]:
            return(1)
        elif hand1[i][0]<hand2[i][0]:
            return(-1)
        else:
            return(0)
    else:
        if score1>score2:
            return(1)
        elif score1<score2:
            return(-1)
        else:
            return(0)

