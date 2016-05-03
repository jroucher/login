Feature: Login section
    @VDCPORTALS-168
    Scenario: [NOK]Login
      Given goto page
        And select language "en"
       When set "name" to "fakeusername"
        And set "password" to "fakeuserpass"
        And login
       Then Show Message "Error in user/password or tenant name"

    @VDCPORTALS-160
    Scenario: [OK]Login
        Given goto page
          And select language "en"
         When set "name" to "Aurigae"
          And set "password" to "AUrig@e123"
          And clear input "tenant"
          And login
         Then Open main section of App
          And userdata in header is equal to "Aurigae (Primary)"
