import org.apache.tika.Tika;

import java.io.*;


public class Principal {

	public static void main(String[] args) {

        String content = null;
        
        
		try {
			content = getTextFromPDF("" + args[0]);
		} catch (Exception e) {
			e.printStackTrace();
		}
        BufferedWriter writer = null;
		try {
			writer = new BufferedWriter(new FileWriter("" + args[1]));
		} catch (IOException e2) {
			e2.printStackTrace();
		}
        try {
			writer.write(content);
		} catch (IOException e1) {
			e1.printStackTrace();
		}
        try {
			writer.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

    private static String getTextFromPDF(String file) {
        try {
            File a = new File(file);
            return new Tika().parseToString(a);
        } catch (final Exception e) {
        	e.printStackTrace();
        }
        return null;
    }

   

}
