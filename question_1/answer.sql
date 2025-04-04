SELECT PROG_NAME.STEP_PROG_NAME
FROM DEPENDENCY_RULES
  INNER JOIN PROG_NAME
ORDER BY DEPENDENCY_RULES.STEP_DEP_ID , DEPENDENCY_RULES.STEP_SEQ_ID
;

-- Limitations
-- The above code displays the result for the STEP_PROG_NAME to be run 1 by 1
-- It is not able to determine which are the STEP_PROG_NAME that can be run in parallel
