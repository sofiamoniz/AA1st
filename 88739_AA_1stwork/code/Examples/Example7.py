"""
AA, December 2020
Assignment 1: Estratégias de Desenvolvimento de Algoritmos 
            - The Longest Common Subsequence Problem
Autor: Ana Sofia Fernandes, 88739
"""

from Recursive.LCS_recursive import LCS_recursive
from Memoization.LCS_memoization_wrapper import LCS_memoization_wrapper
from Dynamic.LCS_dynamic import LCS_dynamic

class Example7:

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

                    Jaro Moynahan sat quietly back down and poured himself another glass of
                    Latonka. The pale green wine had a delicate yet exhilarating taste.
                    It made him think of cool green grapes beaded with dew. On the hot,
                    teeming planet of Mercury it was as refreshing as a cold plunge.

                    He wondered who was putting up the ten thousand Earth notes? Who stood
                    to lose most in case of a revolution? The answer seemed obvious enough.
                    Who, but Albert Peet. Peet controlled the Latonka trade for which there
                    was a tremendous demand throughout the Universe.

                    And what had happened to the girl. Had the rebels abducted her. If
                    so, he suspected that they had caught a tartar. The Red Witch had the
                    reputation of being able to take care of herself.

                    He beckoned a waiter, paid his bill. As the Mercurian started to leave,
                    a thought struck Jaro. These yellow-eyed Mercurians could see as well
                    in the dark as any alley-prowling cat. For centuries they had lived
                    most their lives beneath ground to escape the terrible rays of the
                    sun. Only at night did they emerge to work their fields and ply their
                    trades. He peeled off a bill, put it in the waiter's hands.

                    "What became of the red-headed singer?"

                    The Mercurian glanced at the bill, then back at the Earthman. There was
                    no expression in his yellow eyes.

                    "She and the man, the queer white one who plays the piano, slipped out
                    the gate to the street."

                    Jaro shrugged, dismissed the waiter. He had not expected to get much
                    information from the waiter, but he was not a man to overlook any
                    possibility. If the girl had been abducted, only Mercurians could have
                    engineered it in the dark; and the Mercurians were a clannish lot.

                    Back on the narrow alley-like street Jaro Moynahan headed for his
                    hostelry. By stretching out his arms he could touch the buildings on
                    either side: buildings with walls four feet thick to keep out the
                    heat of the sun. Beneath his feet, he knew, stretched a labyrinth of
                    rooms and passages. Somewhere in those rat-runs was Karfial Hodes, the
                    revolutionist, and the girl.

                    At infrequent intervals green globes cut a hole in the night, casting a
                    faint illumination. He had just passed one of these futile street lamps
                    when he thought he detected a footfall behind him. It was only the
                    whisper of a sound, but as he passed beyond the circle of radiation, he
                    flattened himself in a doorway. Nothing stirred. There was no further
                    sound. Again he started forward, but now he was conscious of shadows
                    following him. They were never visible, but to his trained ears there
                    came stealthy, revealing noises: the brush of cloth against the baked
                    earth walls, the sly shuffle of a step. He ducked down a bisecting
                    alley, faded into a doorway. Immediately all sounds of pursuit stopped.
                    But as soon as he emerged he was conscious again of the followers. In
                    the dense, humid night, he was like a blind man trying to elude the
                    cat-eyed Mercurians.

                    [Illustration: _Jaro Moynahan_]

                    In the East a sullen red glow stained the heavens like the reflection
                    of a fire. The Mercurian dawn was about to break. With an oath, he set
                    out again for his hostelry. He made no further effort to elude the
                    followers.

                        *       *       *       *       *

                    Once back in his room, Jaro Moynahan stripped off his clothes,
                    unbuckled a shoulder holster containing a compressed air slug gun,
                    stepped under the shower. His body was lean and brown as his face
                    and marked with innumerable scars. There were small round puckered
                    scars and long thin ones, and his left shoulder bore the unmistakable
                    brownish patch of a ray burn. Stepping out of the shower, he dried,
                    rebuckled on the shoulder holster, slipped into pajamas. The pajamas
                    were blue with wide gaudy stripes. Next he lit a cigarette and
                    stretching out on the bed began to contemplate his toes with singular
                    interest.

                    He had, he supposed, killed rather a lot of men. He had fought in
                    the deadly little wars of the Moons of Jupiter for years, then the
                    Universal Debacle of 3368, after that the Martian Revolution as well as
                    dozens of skirmishes between the Federated Venusian States. No, there
                    was little doubt but that he had killed quite a number of men. But this
                    business of hunting a man through the rat-runs beneath the city was out
                    of his line.

                    Furthermore, there was something phony about the entire set up.
                    The Mercurians, he knew, had been agitating for freedom for years.
                    Why, at this time when the Earth Congress was about to grant them
                    self-government, should they stage a revolution?

                    A loud, authoritative rapping at the door interrupted further
                    speculation. He swung his bare feet over the edge of the bed, stood
                    up and ground out his cigarette. Before he could reach the door the
                    rapping came again.

                    Throwing off the latch, he stepped back, balancing on the balls of his
                    feet. '''

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

                    Jaro Moynahan refilled their empty glasses. He was a big man, handsome
                    in a gaunt fashion. Only his eyes were different. They were flat and
                    a trifle oblique with straight brows. The pupils were a pale and
                    penetrating blue that could probe like a surgeon's knife. Now he caught
                    the girl's eyes and held them with his own as a man spears a fish.

                    "Why call me all the way from Mars for that? Why not have that gunman
                    at the piano rub Hodes out?"

                    The girl started, glanced at the pianist, said with a shiver: "We can't
                    locate Karfial Hodes. Don't look at me that way, Jaro. You frighten me.
                    I'm telling the truth. We can't find him. That's why we called you.
                    You've got to find him, Jaro. He's stirring up all Mercury."

                    "Who's putting up the money?"

                    "I can't tell you."

                    "Ah," said Jaro Moynahan; "so that's the way it is."

                    "That's the way it is."

                    "There isn't much time," he said after a moment. "The Rains are due any
                    day now."
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

    
    