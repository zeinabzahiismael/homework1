import json
q1="""1)_ A given layer in the architecture can directly communicate with its peer on other end systems.
a)True
b)False
"""

q2="""2)_ In the protocol stack,there can be more than one protocol per layer.
a)True
b)False"""

q3="""3)_ A given layer in the layered model can indirectly communicate with its peer.
a)True
b)False"""

q4="""4)_ Protocol stack is a list of protocols used by a certain system one Protocol per layer.
a)True
b)False"""

q5="""5)_ The application layer of TCP/IP maps to the session presentation and application layers of OSI.
a)True
b)False"""

q6="""6)_ The data link layer is concerned with synchronization of bits.
a)True
b)False"""

q7="""7)_ The delivery of a packet at the network layer is nod-to-nod.
a)True
b)False"""

q8="""8)_ The layering concept hides the specific underlying network technology from the upper layers.
a)True
b)False"""

q9="""9)_ Flow control can be done at data link and network layers.
a)True
b)False"""

q10="""10)_ The peer entities comprising the corresponding layers can be on the same machine.
a)True
b)False"""

q11="""11)_ The 802 specifications define the LANs and WANs standards and technologies.
a)True
b)False"""

q12="""12)_ The data link layer is responsible for data rate control.
a)True
b)False"""

q13="""13)_ The network layer is concerned with routing.
a)True
b)False"""

q14="""14)_ Both data link and network layers can provide flow control.
a)True
b)False"""

q15="""15)_ Encryption is not a function of data link layer.
a)True
b)False"""

q16="""16)_ Error control can be done by data link layer .
a)True
b)False"""

q17="""17)_ Function in peer-to-peer layers are performed at the end user devices .
a)True
b)False"""

q18="""18)_ In some applications,the higher layer encapsulates the lower layer data unit.
a)True
b)False"""

q19="""19)_ A router has more overhead than a bridge.
a)True
b)False"""

q20="""20)_ A tree of hubs can makes a LAN with several collision domains.
a)True
b)False"""

questions_answers={q1:'b',q2:'b',q3:'a',q4:'a',q5:'a',q6:'b',q7:'b',q8:'a',q9:'b',q10:'a',q11:'a',q12:'a',q13:'a',q14:'b',q15:'a',q16:'a',q17:'a',q18:'b',q19:'a',q20:'b'}

zeinab=json.dumps(questions_answers)
with open('zeinab.json','w') as z:
    z.write(zeinab)







