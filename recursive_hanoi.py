def hanoi(n, source, target, auxiliary, moves=[]):
    if n > 0:
        # Déplacer n-1 disques de la source vers le poteau auxiliaire
        hanoi(n-1, source, auxiliary, target, moves)
        
        # Déplacer le n-ème disque de la source vers la cible
        moves.append((source, target))
        
        # Déplacer les n-1 disques du poteau auxiliaire vers la cible
        hanoi(n-1, auxiliary, target, source, moves)

    return moves

# Exemple d'utilisation
nombre_de_disques = 3
mouvements = hanoi(nombre_de_disques, 'A', 'C', 'B')

print(f"Solution pour {nombre_de_disques} disques:")
for move in mouvements:
    print(f"Déplacer de {move[0]} vers {move[1]}")