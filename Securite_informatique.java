/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package securite_informatique;

import java.util.Scanner;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.Arrays;
import java.util.List;

/**
 *
 * @author Glody KHALIFA DAWILI
 */
public class Securite_informatique {

    /**
     * @param args the command line arguments
     */
     public static int[] generKey(int[] mot, int[] permitation) {
        int index = 0;
        int[] tempo = new int[mot.length];
        for (int i = 0; i < permitation.length; i++) {
            index = permitation[i];
            tempo[i] = mot[index];
         //K[i]=K[index];

        }
        mot = tempo;
        return mot;
    }
    public static void main(String[] args) {
        //
        System.out.println("=================================================");
        System.out.println("======= ALGORITHME DE GENERATION DES CLES =======");
        System.out.println("=================================================");
        //
        // lire les élèment de la clé K
        //
        int tabkey[] = new int[8];
        Scanner KGB = new Scanner(System.in);
        for (int i = 0; i < 8; i++) {
            System.out.print("saisissez le bit de position " + i + ":");
            tabkey[i] = KGB.nextInt();
        }
        //

        //Affichage des données de la clé K 
        //
        System.out.print("K = ");
        for (int i = 0; i < 8; i++) {
            System.out.print("|" + tabkey[i] + "|");
        }
        //Lecture des élèments des élèments de la fonction de permutation   
        int tabfonction[] = new int[8];
        System.out.println("");
        for (int j = 0; j < 8; j++) {
            System.out.print("saisissez la valeur de la fonction position " + j + ":");
            tabfonction[j] = KGB.nextInt();
        }
        //

        //Affichage de données de la fonction de permutation 
        //
        System.out.print("Fonction de permutation = ");
        for (int j = 0; j < 8; j++) {
            System.out.print("|" + tabfonction[j] + "|");
        }
        //

        //Application de la fonction de permutation  
        //
        System.out.println("");
        System.out.print("La fonction de permutation devient : " + "|" + tabkey[6] + "||" + tabkey[5] + "||" + tabkey[2] + "||" + tabkey[7] + "||" + tabkey[4] + "||" + tabkey[1] + "||" + tabkey[3] + "||" + tabkey[0] + "|");
        System.out.println("");
        //

        //Affectation K1
        //
        System.out.print("k1 = " + "|" + tabkey[6] + "||" + tabkey[5] + "||" + tabkey[2] + "||" + tabkey[7] + "|");
        System.out.println("");
        //

        //Affectation K2
        //
        System.out.print("k2 = " + "|" + tabkey[4] + "||" + tabkey[1] + "||" + tabkey[3] + "||" + tabkey[0] + "|");
        System.out.println("");
        System.out.print("k'1 = ");
        if (tabkey[6] == tabkey[4]) {
            System.out.print(0 + "||");
        } else {
            System.out.print(1 + "||");
        }
        if (tabkey[5] == tabkey[1]) {
            System.out.print(0 + "||");
        } else {
            System.out.print(1 + "||");
        }
        if (tabkey[2] == tabkey[3]) {
            System.out.print(0 + "||");
        } else {
            System.out.print(1 + "||");
        }
        if (tabkey[7] == tabkey[0]) {
            System.out.print(0 + "||");
        } else {
            System.out.print(1 + "||");
            System.out.println("");
        }
        System.out.print("k'2 = ");
        if (tabkey[6] == tabkey[4]) {
            System.out.print(1 + "||");
        } else if (tabkey[6] == 0 && tabkey[4] == 0) {
            System.out.print(0 + "||");
        } else {
            System.out.print(0 + "||");
        }
        if (tabkey[5] == tabkey[1]) {
            System.out.print(1 + "||");
        } else if (tabkey[5] == 0 && tabkey[1] == 0) {
            System.out.print(0 + "||");
        } else {
            System.out.print(0 + "||");
        }
        if (tabkey[2] == tabkey[3]) {
            System.out.print(1 + "||");
        } else if (tabkey[2] == 0 && tabkey[3] == 0) {
            System.out.print(0 + "||");
        } else {
            System.out.print(0 + "||");
        }
        if (tabkey[7] == tabkey[0]) {
            System.out.print(1 + "||");
        } else if (tabkey[7] == 0 && tabkey[0] == 0) {
            System.out.print(0 + "||");
        } else {
            System.out.print(0 + "||");
            System.out.println("");
        }
        //

        //Application de decalage à gauche pour k1
        //
        System.out.println("k1 = G2(k1) = " + "|" + tabkey[2] + "||" + tabkey[7] + "||" + tabkey[6] + "||" + tabkey[5] + "|");
        //

        //Application de decalage à droite pour k2
        //
        System.out.println("k2 = D1(k2) = " + "|" + tabkey[0] + "||" + tabkey[4] + "||" + tabkey[1] + "||" + tabkey[3] + "|");
        //

        //
        System.out.println("");
        //
        System.out.println("=================================================");
        System.out.println("=========== ALGORITHME DE CHIFFREMENT ===========");
        System.out.println("=================================================");
        //
        // lire les élèments de bloc N de 8 bits
        //
        int blocN[] = new int[8];
        Scanner KGBA = new Scanner(System.in);
        for (int k = 0; k < 8; k++) {
            System.out.print("saisissez le bit de N  " + k + " ème position:");
            blocN[k] = KGBA.nextInt();
            //    
        }
        //Affichage des données de bloc N 
        //
        System.out.print("N = ");
        for (int k = 0; k < 8; k++) {
            System.out.print("|" + blocN[k] + "|");
        }
        //
        //Lecture des élèments des élèments de la fonction de permutation PI
        int tabfctPI[] = new int[8];
        System.out.println("");
        for (int l = 0; l < 8; l++) {
            System.out.print("saisissez la valeur de la fonction PI  " + l + " ème position:");
            tabfctPI[l] = KGBA.nextInt();
        }
        //Affichage de données de la fonction de permutation PI
        //
        System.out.print("Fonction de permutation PI = ");
        for (int l = 0; l < 8; l++) {
            System.out.print("|" + tabfctPI[l] + "|");
        }
        //Application de la fonction de permutation  
        //
        System.out.println("");
        System.out.print("La fonction de permutation devient : " + "|" + blocN[4] + "||" + blocN[6] + "||" + blocN[0] + "||" + blocN[2] + "||" + blocN[7] + "||" + blocN[3] + "||" + blocN[1] + "||" + blocN[5] + "|");
        System.out.println("");
        //
        //
        //Division de N en deux blocs de 4 bits Go et Do
        //
        //Affectation Go
        //
        System.out.print("Go = " + "|" + blocN[4] + "||" + blocN[6] + "||" + blocN[0] + "||" + blocN[2] + "|");
        System.out.println("");
        //
        //Affectation Do
        //
        System.out.print("Do = " + "|" + blocN[7] + "||" + blocN[3] + "||" + blocN[1] + "||" + blocN[5] + "|");
        System.out.println("");
        //
        //Premier Round, calcul de G1 et D1
        //
    }

}
