# CS5 Gold, hw1pr3
# Filename: hw1pr3.py
# Name: Joe Konieczny
# Problem description: Function Frenzy!

#
# leng example from class
#
def leng( s ):
    """ leng outputs the length of s
            input: s, which can be a string or list

    """
    if s == '' or s == []:
        return 0
    else:
        return 1 + leng( s[1:])
def mult (n,m):
    """ mult outputs the product of
        input: n, m
    """
    if m == 0 or n == 0:
        return 0
    elif m<0:
        return -n + mult (n,m+1)
    else:
        return n + mult (n,m-1)
def dot (L,K):
    """ should output the dot product of the lists L and K"""
    if len(L) != len(K):
        return 0
    if L == [] or K == []:
        return 0
    else:
        return L[0]*K[0] + dot (L[1:],K[1:])
def ind(e,L):
    """takes in a sequence L and an element e"""
    if e not in L:
        return len(L)
    if L[0] == e:
        return 0
    else:
        return ind(e,L[1:]) + 1
def letterScore(let):
    """Returns the 'scrabble' value of the one-character string let
    """
    if let in 'AaEeIiLlNnOoRrSsTtUu':
        return 1
    elif let in 'DdGg':
        return 2
    elif let in 'BbCcMmPp':
        return 3
    elif let in 'FfHhVvWwYy':
        return 4
    elif let in 'Kk':
        return 5
    elif let in 'XxJj':
        return 8
    elif let in 'QqZz':
        return 10
    else:
        return 0

def scrabbleScore(S):
    """Returns the 'scrabble' value of the multi-character string S
    """
    if S == '':
        return 0
    else:
        return letterScore(S[0]) + scrabbleScore(S[1:])

def transcribe(S):
    """ Converts a DNA string an RNA string
    """
    if S == '':
        return ''
    else:
        return one_dna_to_rna(S[0]) + transcribe(S[1:])

def one_dna_to_rna( c ):
    """ converts a single-character c from DNA
        nucleotide to complementary RNA nucleotide """
    if c == 'A': return 'U'
    elif c == 'C': return 'G'
    elif c == 'G': return 'C'
    elif c == 'T': return 'A'
    else:
        return ''

def pigletLatin(s):
    """ converts the string s into Dodds' 'piglet latin' language
    """
    if s == '': return ''
    elif s[0] in 'AaEeIiOoUu': return s[0:] + 'way'
    elif s[0] in 'BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxYyZz': return s[1:] + s[0] + 'ay'

def pigLatin(s):
    """ Creates a fully formed Pig Latin string with accurate handling of multiple frontal consonants
    """
    if s == '':
        return ''
    elif s[0] in 'Yy' and s[1] in 'BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxYyZz' : return s + 'way'
    elif s[0] in 'Yy' and s[1] in 'AaEeIiOoUu': return vowels(s) + initial_consonants(s) + 'ay'
    else:
        return  vowels(s) + initial_consonants(s) + 'ay'

def initial_consonants(s):
    """ Helps the full Pig Latin function
    """
    if s[0] in 'AaEeIiOoUu': return ''
    else:
        return s[0] + initial_consonants(s[1:])

def vowels(s):
    """ Defines the intial values to aid function pigLatin(s)
    """
    if s[0] in 'AaEeIiOoUu': return s
    else:
        return vowels(s[1:])

#
# I finished all of the CodingBat STRING problems.
#

#
# I finished all of the CodingBat LIST problems.
#