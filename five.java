public class MainActivity extends AppCompatActivity {
    private ExecutorService executorService;
    private Handler mainHandler;
    private EditText phoneNumber, messageContent;
    private Button sendButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        executorService = Executors.newSingleThreadExecutor();
        mainHandler = new Handler(Looper.getMainLooper());

        phoneNumber = findViewById(R.id.phoneNumber);
        messageContent = findViewById(R.id.messageContent);
        sendButton = findViewById(R.id.sendMessage);

        if (ContextCompat.checkSelfPermission(this, Manifest.permission.SEND_SMS)
                != PackageManager.PERMISSION_GRANTED) {
            ActivityCompat.requestPermissions(this,
                    new String[]{Manifest.permission.SEND_SMS}, 1);
        }

        sendButton.setOnClickListener(v -> {
            String phone = phoneNumber.getText().toString().trim();
            String message = messageContent.getText().toString().trim();

            if (phone.isEmpty() || message.isEmpty()) {
                Toast.makeText(MainActivity.this, "Please enter both phone number and message", Toast.LENGTH_SHORT).show();
                return;
            }

            sendSmsAsync(phone, message);
        });
    }

    private void sendSmsAsync(String phone, String message) {
        executorService.execute(() -> {
            try {
                SmsManager sms = SmsManager.getDefault();
                sms.sendTextMessage(phone, null, message, null, null);
                mainHandler.post(() ->
                        Toast.makeText(MainActivity.this, "SMS sent successfully", Toast.LENGTH_SHORT).show());
            } catch (Exception e) {
                e.printStackTrace();
                mainHandler.post(() ->
                        Toast.makeText(MainActivity.this, "SMS failed: " + e.getMessage(), Toast.LENGTH_SHORT).show());
            }
        });
    }
}