/*
https://app.codesignal.com/arcade/graphs-arcade/kingdom-roads/nCMisf4ZKpDLdHevE/solutions?solutionId=rubW82sSG8nuvn4CL
Each city has the same number of incoming and outgoing roads. As the Hand of the King, you're the one who he has decreed must check his calculations.
*/

package graphs.citiesSameNumOfVertices_codesignal;

import java.util.*;

public class hashmap {

    boolean newRoadSystem(boolean[][] roadRegister) {

        Map<Integer, Integer> cityRoads = new HashMap<Integer, Integer>();
        
        int numberOfCities = roadRegister.length;
        
        // For each city
        for (int city=0; city<numberOfCities; city++) {
            // Traverse columns & count roads
            for (int col=0; col<numberOfCities; col++) {
                if (roadRegister[city][col]) {
                    cityRoads.put(city,cityRoads.get(city) == null ? 1 : cityRoads.get(city) + 1);                
                }
            }
            // Traverse rows & discount roads
            for (int row=0; row<numberOfCities; row++) {
                if (roadRegister[row][city]) {
                    cityRoads.put(city,cityRoads.get(city) == null ? -1 : cityRoads.get(city) - 1);                
                }
            }
        }
        
        // If counter for any reason was not empty, means there is a disproportion of input/output in roads
        for (Map.Entry<Integer,Integer> city : cityRoads.entrySet()) {
            if (city.getValue() > 0) {
                return false;
            }
        }
        
        return true;
    }

}