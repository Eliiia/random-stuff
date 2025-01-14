        B bubble_sort

;tis_array      DEFW    2,6,4,6,2,1,1,3,2
;tis_array      DEFW    1,2,3,4,5,6,7,8,9
;tis_array      DEFW    9,8,7,6,5,4,3,2,1
tis_array       DEFW    9,2,1,4,3,6,5,8,7

        ALIGN

bubble_sort
        ; R1 = pointer to arr
        ; R2 = offset
        ; R3 = first num read
        ; R4 = second num read
        ; R5 = iterations

        ADRL R1,tis_array ; get address of array
        MOV R5, #0 ; reset R5

bubble_sort_loop_start
        MOV R2, #0 ; reset offset
        ADD R5, R5, #1

        CMP R5, #10 ; if (enough iterations) { ; (i think this would be 9 iterations)
        BEQ bubble_sort_loop_exit ; go to bubble_sort_loop_exit
        ; }

bubble_sort_loop_main
        CMP R2, #32 ; if R2 == 9 {
        BEQ bubble_sort_loop_start ; restart loop
        ; }

        LDR R3, [R1, R2] ; read first element
        ADD R2, R2, #4 ; increment offset
        LDR R4, [R1, R2] ; read second element

        CMP R3, R4 ; if (first > second) {
        STRGT R3, [R1, R2] ; swap
        SUBGT R2, R2, #4
        STRGT R4, [R1, R2]
        ADDGT R2, R2, #4
                    ; }
        
        B bubble_sort_loop_main; go back to loop

bubble_sort_loop_exit
        SWI 2