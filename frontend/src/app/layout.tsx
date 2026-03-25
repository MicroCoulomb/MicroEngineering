import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "MicroPrelegal | Platform Foundation",
  description: "V1 platform foundation with fake login, FastAPI runtime, and NDA workspace.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className="h-full antialiased">
      <body className="min-h-full flex flex-col">{children}</body>
    </html>
  );
}
