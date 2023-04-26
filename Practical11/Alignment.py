import blosum as bl
matrix = bl.BLOSUM(62)
seq1 = open('C:/Users/Asus/Downloads/ACE2_human.fa')
seq2 = open('C:/Users/Asus/Downloads/ACE2_mouse.fa')
seq3 = open('C:/Users/Asus/Downloads/ACE2_cat.fa')
q1 = ''
q2 = ''
q3 = ''
for line in seq1:
    if not line.startswith('>'):
        q1 = line.strip()
for line in seq2:
    if not line.startswith('>'):
        q2 = line.strip()
for line in seq3:
    if not line.startswith('>'):
        q3 = line.strip()
list1 = list(q1)
list2 = list(q2)
list3 = list(q3)

def compare(s1,s2):
    num = 0
    score = 0
    for i in range(len(s1)):
        score += matrix[s1[i]][s2[i]]
        if s1[i] == s2[i]:
            num += 1
    percentage = num/len(s1)
    print(percentage)
    return score
print(compare(list1, list2))
print(compare(list1, list3))
print(compare(list2, list3))
