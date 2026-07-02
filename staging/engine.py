from .rules import COLON_M0_MATRIX



def calculate_stage(
        cancer,
        edition,
        T,
        N,
        M
):


    if cancer != "colon":

        return {

            "stage":"Unsupported cancer"

        }



    if edition != "AJCC8":

        return {

            "stage":"Unsupported edition"

        }



    # ==========================
    # M CATEGORY LOGIC
    # ==========================


    if M == "M1a":


        return {

            "stage":"Stage IVA",

            "reason":
            "M1a: metastasis to one distant site or organ without peritoneal metastasis"

        }



    if M == "M1b":


        return {

            "stage":"Stage IVB",

            "reason":
            "M1b: metastasis to two or more distant sites/organs without peritoneal metastasis"

        }



    if M == "M1c":


        return {

            "stage":"Stage IVC",

            "reason":
            "M1c: peritoneal surface metastasis"

        }




    # ==========================
    # M0 T/N MATRIX
    # ==========================


    if M == "M0":



        try:


            stage = COLON_M0_MATRIX[N][T]



            return {


                "stage": stage,


                "reason":
                f"{T} + {N} + M0 according to AJCC 8th edition colon cancer staging"

            }



        except KeyError:


            return {


                "stage":"Not classified",

                "reason":
                "TNM combination not found"

            }





    return {


        "stage":"Invalid M category"

    }