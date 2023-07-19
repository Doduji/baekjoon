def solution(letter):
    answer = ''
    answer_list = []
    morse = { 
        '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
        '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
        '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
        '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
        '-.--':'y','--..':'z'
    }

    div = list(letter.split())
    for i in range(0, len(div)) : 
        answer_list.append(morse[div[i]])

    answer = ''.join(str(s) for s in answer_list)
    
    return answer