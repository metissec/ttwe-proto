def setup_host():
  
  signal.signal(signal.SIGINT, signal_handler)

  parser = argparse.ArgumentParser()
  parser.add_argument("-v", "--verbose", action="store_true", 
      help="turn on verbose output of USB communication")
  parser.add_argument("--OUT", type=int, default=1, help="peripheral OUT Endpoint number")
  parser.add_argument("--IN", type=int, default=2, help="peripheral IN Endpoint number")
  parser.add_argument("--IN2", type=int, default=3, help="peripheral IN2 Endpoint number")

  args = parser.parse_args()

  #Initialize FET and set baud rate
  client=GoodFETMAXUSBHost();
  client.serInit()

  client.MAXUSBsetup();

  print('host init')
  # hub detects device
  client.hostinit(HostRelayDevice(args.verbose, OUT_EP=args.OUT, 
    IN_EP=args.IN, IN2_EP=args.IN2)); 
  client.usbverbose=False;

  print('device detect')
  # detect the device-low or full speed
  client.detect_device(); 
  time.sleep(0.2); 

  # reset bus, set address 0 
  client.soft_enumerate() 

  client.reset_bus()

  print('done enumerating, deferring to irqs')
  client.service_irqs()
  client.usb_disconnect()
  
def setup_client():
  
  signal.signal(signal.SIGINT, signal_handler)

  parser = argparse.ArgumentParser()
  parser.add_argument("-v", "--verbose", action="store_true", 
      help="turn on verbose output of USB communication")
  parser.add_argument("--OUT", type=int, default=1, help="peripheral OUT Endpoint number")
  parser.add_argument("--IN", type=int, default=2, help="peripheral IN Endpoint number")
  parser.add_argument("--IN2", type=int, default=3, help="peripheral IN2 Endpoint number")

  args = parser.parse_args()

  #Initialize FET and set baud rate
  client=GoodFETMAXUSBHost();
  client.serInit()

  client.MAXUSBsetup();

  print('host init')
  # hub detects device
  client.hostinit(HostRelayDevice(args.verbose, OUT_EP=args.OUT, 
    IN_EP=args.IN, IN2_EP=args.IN2)); 
  client.usbverbose=False;

  print('device detect')
  # detect the device-low or full speed
  client.detect_device(); 
  time.sleep(0.2); 

  # reset bus, set address 0 
  client.soft_enumerate() 

  client.reset_bus()

  print('done enumerating, deferring to irqs')
  client.service_irqs()
  client.usb_disconnect()
  
  
