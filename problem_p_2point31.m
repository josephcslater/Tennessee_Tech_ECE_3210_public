syms x y G1 H1 G2 H2 G3 H3 G4 H4 G5 G6 R1 Y1 Y2 X1
eqn1 = R1-H1*Y1-X1 == 0
eqn2 = X1*G1+G3*H2*Y2-Y1/G2==0
eqn3 = Y2*H2*G5+G4/G2*Y1-Y2/G6
soln = solve([eqn1, eqn2, eqn3], [X1 Y1 Y2])
T11 = soln.Y1/R1
T12 = soln.Y2/R1