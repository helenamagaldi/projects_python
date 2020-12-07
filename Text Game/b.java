HashSet<Integer> h = new HashSet<>(); 
       
        node present = head; 
        node preceding = null; 
        while (present != null)  
        { 
            int presentval = present.value; 
              
            if (h.contains(presentval)) { 
                preceding.next = present.next; 
            } else { 
                h.add(presentval); 
                preceding = present; 
            } 
            present = present.next; 
        } 
   
    } 