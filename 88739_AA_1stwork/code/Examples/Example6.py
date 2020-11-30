"""
AA, December 2020
Assignment 1: Estratégias de Desenvolvimento de Algoritmos 
            - The Longest Common Subsequence Problem
Autor: Ana Sofia Fernandes, 88739
"""

from Recursive.LCS_recursive import LCS_recursive
from Memoization.LCS_memoization_wrapper import LCS_memoization_wrapper
from Dynamic.LCS_dynamic import LCS_dynamic

class Example6:

    def __init__(self):
        self.seqA = '''"No," the girl replied. "But we think he's here in the city."

                    "Why? What makes you think that?"

                    "He was seen," she began, then stopped with a gasp.

                    The lights had gone out.

                    It was as unexpected as a shot in the back. One moment the garden was
                    glowing in light, the next the hot black night swooped down on the
                    revelers, pressing against their eyes like dark wool. The fans about
                    the walls slowed audibly and stopped. It grew hotter, closer.

                    Jaro Moynahan slipped sideways from the table. He felt something brush
                    his sleeve. Somewhere a girl giggled.

                    "What's coming off here?" growled a petulant male voice. Other voices
                    took up the plaint.

                    Across the table from Jaro there was the feel of movement; he could
                    sense it. An exclamation was suddenly choked off as if a hand had been
                    clamped over the girl's mouth.

                    "Red!" said Jaro in a low voice.

                    There was no answer.

                    "Red!" he repeated, louder.

                    Unexpectedly, the deep, ringing voice of Mercury Sam boomed out from
                    the stage.

                    "It's all right. The master fuse blew out. The lights will be on in a
                    moment."

                    On the heels of his speech the lights flashed on, driving the night
                    upward. The fans recommenced their monotonous whirring.

                    Jaro Moynahan glanced at the table. The red-headed singer was gone. So
                    was the pianist.
                    '''

        self.seqB = ''' The night was very hot; but then it is always hot on Mercury, the
                    newest, the wildest, the hottest of Earth's frontiers. Fans spaced
                    about the garden's walls sluggishly stirred the night air, while the
                    men and women sitting at the tables drank heavily of Latonka, the
                    pale green wine of Mercury. Only the native waiters, the enigmatic,
                    yellow-eyed Mercurians, seemed unaffected by the heat. They didn't
                    sweat at all.

                    Up on the stage the singer was about to begin another number when she
                    stiffened.

                    "Here he is," she said to the pianist without moving her lips.

                    The pianist swung around on his stool, lifted his black eyes to the
                    gate leading to the street.

                    Just within the entrance, a tall, thin man was standing. He looked like
                    a gaunt gray wolf loitering in the doorway. His white duraloes suit
                    hung faultlessly. His black hair was close-cropped, his nose thin and
                    aquiline. For a moment he studied the crowded garden before making his
                    way to a vacant table.

                    "Go on," said the pianist in a flat voice.

                    The red-head shivered. Stepping from the stage she picked her way
                    through the tables until she came to the one occupied by the newcomer.

                    "May I join you?" she asked in a low voice.

                    The man arose. "Of course. I was expecting you. Here, sit down." He
                    pulled out a chair, motioned for the waiter. The Mercurian, his yellow
                    incurious eyes like two round topazes, sidled up. "Bring us a bottle
                    of Latonka from the Veederman region, well iced." The waiter slipped
                    away.

                    "So," said the red-head; "you have come. I did not think you would be
                    in time." Her hands were clenched in her lap. The knuckles were white.

                    The man said nothing.

                    "I did not want to call you in, Jaro Moynahan." It was the first time
                    she had used his name. "You have the reputation of being unpredictable.
                    I don't trust you, but since...."

                        *       *       *       *       *

                    She stopped as the waiter placed glasses on the table and deftly poured
                    the pale green wine. The man, Jaro Moynahan, raised his glass.

                    "Here's to the revolution," he said. His low voice carried an odd,
                    compelling note. His eyes, light blue and amused, were pale against his
                    brown face.

                    The girl drew in her breath.

                    "No! Mercury is not ready for freedom. Only a handful of fanatics are
                    engineering the revolution. The real Mercurian patriots are against
                    it, but they are afraid to protest. You've got to believe me. The
                    revolution is scheduled to break during the Festival of the Rains. If
                    it does, the Terrestrials here will be massacred. The Mercurians hate
                    them. We haven't but a handful of troops."

                    Jaro Moynahan wiped the sweat from his forehead with a fine duraweb
                    handkerchief. "I had forgotten how abominably hot it can be here."

                    The girl ignored the interruption. "There is one man; he is the leader,
                    the very soul of the revolution. The Mercurians worship him. They will
                    do whatever he says. Without him they would be lost. He is the rebel,
                    Karfial Hodes. I am to offer you ten thousand Earth notes to kill
                    Karfial Hodes."
                    '''
        

    def chose_alg(self,chosen, show=None):
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
            if show == "-s":
                dynamic.get_lcs_longest_subsquence()

    
    