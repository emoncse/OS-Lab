male(abdullah).
male(afsar).
male(johurul).
male(sujon).
male(imran).
male(rupak).
male(alamin).
male(sakil).
male(shuvo).
male(anik).
male(shamim).
male(kibria).
male(manik).
male(fahim).
male(shohag).
male(milon).
male(emon).
male(pranto).
male(ali).
male(amin).
male(sabbir).
male(suman).
male(ruhul).
male(mirza).
male(atik).
male(masud).


female(moriam).
female(sufia).
female(momena).
female(jesmin).
female(pori).
female(moni).
female(kajol).
female(tanni).
female(proma).
female(raisa).
female(pakhi).
female(mohona).
female(bristy).
female(priya).
female(beauty).
female(susmita).
female(kotha).
female(moyna).
female(dristi).



father(abdullah,afsar).
father(abdullah,johurul).
father(afsar,sujon).
father(afsar,imran).
father(sujon,sakil).
father(imran,shuvo).
father(sakil,kibria).
father(sakil,manik).
father(kibria,emon).
father(manik,pranto).
father(manik,ali).
father(pranto,ruhul).

father(johurul,alamin).
father(johurul,rupak).

father(alamin,anik).
father(anik,fahim).
father(anik,shohag).
father(fahim,amin).
father(amin,mirza).
father(shohag,sabbir).
father(sabbir,atik).

father(rupak,shamim).
father(shamim,milon).
father(milon,suman).
father(suman,masud).


mother(moriam,afsar).
mother(moriam,johurul).
mother(sufia,sujon).
mother(sufia,imran).
mother(jesmin,sakil).
mother(pori,shuvo).
mother(tanni,kibria).
mother(tanni,manik).
mother(pakhi,emon).
mother(mohona,pranto).
mother(mohona,ali).
mother(susmita,ruhul).

mother(momena,alamin).
mother(momena,rupak).

mother(moni,anik).
mother(proma,fahim).
mother(proma,shohag).
mother(bristy,amin).
mother(kotha,mirza).
mother(priya,sabbir).
mother(moyna,atik).

mother(kajol,shamim).
mother(raisa,milon).
mother(beauty,suman).
mother(dristi,masud).

/*rules*/

parent(X,Y):-
     mother(X,Y);
     father(X,Y).

sibling(X,Y):-
    parent(Z,X),
    parent(Z,Y),
    X\=Y.

sibling(Y,X):-
    parent(Z,X),
    parent(Z,Y),
    X\=Y.

grandparent(X,Y):-
     parent(Z,Y),
     parent(X,Z).


greatgrandparent(X,Y):-
    parent(X,P),
    parent(P,Z),
    parent(Z,Y).

greatgreatgrandparent(X,Y):-
     parent(A,Y),
     parent(B,A),
     parent(C,B),
     parent(X,C).

firstcousin(X,Y):-
    parent(Z,X),
    parent(W,Y),
    sibling(Z,W).
firstcousin(Y,X):-
    parent(Z,X),
    parent(W,Y),
    sibling(Z,W).

secondcousin(X,Y):-
    greatgrandparent(Z,X),
    greatgrandparent(Z,Y),
    \+firstcousin(X,Y),
    \+sibling(X,Y),
    X\=Y.

thirdcousin(X,Y):-
    greatgreatgrandparent(Z,X),
    greatgreatgrandparent(Z,Y),
    \+firstcousin(X,Y),
    \+secondcousin(X,Y),
    \+sibling(X,Y),
    X\=Y.

firstcousin_onceremoved(X,Y):-
    parent(Z,Y),
    firstcousin(X,Z).
firstcousin_onceremoved(X,Y):-
    parent(Z,X),
    firstcousin(Z,Y).

firstcousin_twiceremoved(X,Y):-
    firstcousin(X,Z),
    grandparent(Z,Y).
firstcousin_twiceremoved(X,Y):-
    firstcousin(Z,Y),
    grandparent(Z,X).

secondcousin_onceremoved(X,Y):-
     parent(Z,Y),
     secondcousin(X,Z).
secondcousin_onceremoved(X,Y):-
     parent(Z,X),
     secondcousin(Z,Y).

secondcousin_twiceremoved(X,Y):-
     grandparent(Z,Y),
     secondcousin(X,Z).
secondcousin_twiceremoved(X,Y):-
     grandparent(Z,X),
     secondcousin(Z,Y).

thirdcousin_onceremoved(X,Y):-
     parent(Z,Y),
     thirdcousin(X,Z).
thirdcousin_onceremoved(X,Y):-
     parent(Z,X),
     thirdcousin(Z,Y).

thirdcousin_twiceremoved(X,Y):-
     grandparent(Z,Y),
     thirdcousin(X,Z).
thirdcousin_twiceremoved(X,Y):-
     grandparent(Z,X),
     thirdcousin(Z,Y).

predecessor(X,Z) :- parent(X,Z).

predecessor(X,Z) :- parent(X,Y), predecessor(Y,Z).
