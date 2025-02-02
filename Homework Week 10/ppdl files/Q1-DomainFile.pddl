(define (domain logistic-domain)
    (:predicates  
            (package ?x) 
            (location ?y) 
            (truck ?z)
            (at-location ?x ?y) 
            (carry ?x ?z) 
      )

  (:action load 
    :parameters (?x ?z)
      :precondition (and 
                      (package ?x)
                      (truck ?z)
                      (not (carry ?x ?z))
                    )       
      :effect       (and
                      (carry ?x ?z)
                    )
  )
  (:action unload :parameters (?x ?z)
      :precondition (and 
                      (package ?x)
                      (truck ?z)
                      (carry ?x ?z)
                    )       
      :effect       (and
                      (not (carry ?x ?z))
                    )
  )

  (:action movewithpackage :parameters (?x ?y1 ?y2 ?z)
      :precondition (and 
                      (location ?y1)
                      (location ?y2)
                      (package ?x)
                      (truck ?z)
                      (at-location ?x ?y1)
                      (at-location ?z ?y1)
                      (carry ?x ?z)
                    )       
      :effect       (and
                      (not (at-location ?x ?y1))
                      (not (at-location ?z ?y1))
                      (at-location ?x ?y2)
                      (at-location ?z ?y2)
                    )
  )
  (:action movewithoutpackage :parameters (?y1 ?y2 ?z)
      :precondition (and 
                      (location ?y1)
                      (location ?y2)
                      (truck ?z)
                      (at-location ?z ?y1)
                    )       
      :effect       (and
                      (not (at-location ?z ?y1))
                      (at-location ?z ?y2)
                    )
  )

)


