(define (domain LogisticDomain)

(: predicates 
            (PACKAGE ?x) 
            (LOCATION ?y) 
            (TRUCK ?z)
            (package-at-location ?x ?y) 
            (truck-at-location ?z ?y)
            (carry ?x ?z) 

  (:action load :parameters (?x, ?z)
      :precondition (and 
                      (PACKAGE ?x)
                      (TRUCK ?z)
                      (not (carry ?x ?z))
                    )       
      :effect       (and
                      (carry ?x ?z)
      )
  )

  (:action unload :parameters (?x, ?z)
      :precondition (and 
                      (PACKAGE ?x)
                      (TRUCK ?z)
                      (carry ?x ?z)
                    )       
      :effect       (and
                      (not (carry ?x ?z))
                    )
  )

  (:action movewithpackage :parameters (?x, ?y1, ?y2, ?z)
      :precondition (and 
                      (PACKAGE ?x)
                      (LOCATION ?y1)
                      (LOCATION ?y2)
                      (TRUCK ?z)
                      (package-at-location ?x ?y1)
                      (truck-at-location ?x ?y1)
                    )       
      :effect       (and
                      (not (package-at-location ?x ?y1))
                      (not (truck-at-location ?x ?y1))
                      (package-at-location ?x ?y2)
                      (truck-at-location ?x ?y2)
                    )
  )

  (:action movewithoutpackage :parameters (?x, ?y1, ?y2, ?z)
      :precondition (and 
                      (PACKAGE ?x)
                      (LOCATION ?y1)
                      (LOCATION ?y2)
                      (TRUCK ?z)
                      (truck-at-location ?x ?y1)
                    )       
      :effect       (and
                      (not (truck-at-location ?x ?y1))
                      (truck-at-location ?x ?y2)
                    )
  )
)


