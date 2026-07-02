from .engine import calculate_stage



def stage_colon(T,N,M):


    return calculate_stage(

        cancer="colon",

        edition="AJCC8",

        T=T,

        N=N,

        M=M

    )