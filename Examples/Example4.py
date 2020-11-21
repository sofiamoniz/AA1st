"""
AA, December 2020
Assignment 1: Estratégias de Desenvolvimento de Algoritmos 
            - The Longest Common Subsequence Problem
Autor: Ana Sofia Fernandes, 88739
"""

from Recursive.LCS_recursive import LCS_recursive
from Memoization.LCS_memoization_wrapper import LCS_memoization_wrapper
from Dynamic.LCS_dynamic import LCS_dynamic

class Example4:

    def __init__(self):
        self.seqA = '''ACT I

            SCENE I. Elsinore. A platform before the Castle.

            Enter Francisco and Barnardo, two sentinels.

            BARNARDO. Who’s there?

            FRANCISCO. Nay, answer me. Stand and unfold yourself.

            BARNARDO. Long live the King!

            FRANCISCO. Barnardo?

            BARNARDO. He.

            FRANCISCO. You come most carefully upon your hour.

            BARNARDO. ’Tis now struck twelve. Get thee to bed, Francisco.

            FRANCISCO. For this relief much thanks. ’Tis bitter cold, And I am sick
            at heart.

            BARNARDO. Have you had quiet guard?

            FRANCISCO. Not a mouse stirring.

            BARNARDO. Well, good night. If you do meet Horatio and Marcellus, The
            rivals of my watch, bid them make haste.

            Enter Horatio and Marcellus.

            FRANCISCO. I think I hear them. Stand, ho! Who is there? '''

        self.seqB = ''' MARCELLUS. Holla, Barnardo!

                    BARNARDO. Say, what, is Horatio there?

                    HORATIO. A piece of him.

                    BARNARDO. Welcome, Horatio. Welcome, good Marcellus.

                    MARCELLUS. What, has this thing appear’d again tonight?

                    BARNARDO. I have seen nothing.

                    MARCELLUS. Horatio says ’tis but our fantasy, And will not let belief
                    take hold of him Touching this dreaded sight, twice seen of us.
                    Therefore I have entreated him along With us to watch the minutes of
                    this night, That if again this apparition come He may approve our eyes
                    and speak to it.

                    HORATIO. Tush, tush, ’twill not appear.

                    BARNARDO. Sit down awhile, And let us once again assail your ears, That
                    are so fortified against our story, What we two nights have seen.

                    HORATIO. Well, sit we down, And let us hear Barnardo speak of this.
                    '''
        

    def chose_alg(self,chosen):
        if chosen == "-r":
            #TODO Escrever para ficheiro
            recursive = LCS_recursive(self.seqA,self.seqB)
            recursive.get_lcs_len_recursive()
        elif chosen == "-m":
            memoization = LCS_memoization_wrapper(self.seqA,self.seqB)
            memoization.get_lcs_len_memoization()
        elif chosen == "-d":
            dynamic = LCS_dynamic(self.seqA, self.seqB)
            dynamic.get_lcs_len_dynamic()

    
    