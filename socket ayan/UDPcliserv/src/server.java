import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;

import java.util.StringTokenizer;

 class server {

	public static void main(String args[]) throws IOException {
		int num1,num2,op,tmp;
		DatagramSocket ds=new DatagramSocket(321);
		
		byte[] b1=new byte[1024];
		byte[] bn=new byte[1024];
		
		DatagramPacket dp=new DatagramPacket(b1,b1.length);
		ds.receive(dp);
		String st=new String(dp.getData());
		
		DatagramPacket dp2=new DatagramPacket(bn,bn.length);
		ds.receive(dp2);
		
		String inp=new String(dp2.getData(),0,dp2.getLength());
		
		StringTokenizer str = new StringTokenizer(inp);
		
		num1=Integer.parseInt(str.nextToken());
		num2=Integer.parseInt(str.nextToken());
		op=Integer.parseInt(str.nextToken());
		//int res=num*2;
		
		switch(op) {
		case 1:
			tmp=num1+num2;
			break;
		case 2:
			tmp=(num1>num2)?num1-num2:num2-num1;
			break;
		case 3:
			tmp=num1*num2;
			break;
		case 4:
			tmp=(num1>num2)?num1/num2:num2/num1;
			break;
		default:
				tmp=0;
				System.out.println("Wrong operation!!");
		}
		
		st=(st + " from Server").trim();
		byte[] b2=st.getBytes();
		InetAddress ia=InetAddress.getLocalHost();
		
		String res = Integer.toString(tmp);
		
		DatagramPacket dp1,dpres;
		
		dp1=new DatagramPacket(b2,b2.length,ia,dp.getPort());
		ds.send(dp1);
		
		b2=res.getBytes();
		dpres=new DatagramPacket(b2,b2.length,ia,dp.getPort());
		ds.send(dpres);
		
		ds.close();
	}
}
