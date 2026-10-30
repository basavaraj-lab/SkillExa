import React, { useState } from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  Platform,
  Linking,
} from 'react-native';
import { Feather } from '@expo/vector-icons';

interface MarkdownRendererProps {
  content: string;
  isUser?: boolean;
}

// Token types for inline parsing
type InlineToken =
  | { type: 'text'; text: string }
  | { type: 'bold'; text: string }
  | { type: 'italic'; text: string }
  | { type: 'code'; text: string }
  | { type: 'link'; text: string; url: string }
  | { type: 'math'; text: string };

export function MarkdownRenderer({ content, isUser = false }: MarkdownRendererProps) {
  if (isUser) {
    return <Text style={styles.userText}>{content}</Text>;
  }

  const blocks = parseMarkdownBlocks(content);

  return (
    <View style={styles.container}>
      {blocks.map((block, idx) => (
        <React.Fragment key={idx}>{renderBlock(block, idx)}</React.Fragment>
      ))}
    </View>
  );
}

// -------------------------------------------------------------
// BLOCK PARSER
// -------------------------------------------------------------
type Block =
  | { type: 'heading'; level: number; text: string }
  | { type: 'code'; language: string; code: string }
  | { type: 'bullet'; items: string[] }
  | { type: 'numbered'; items: string[] }
  | { type: 'alert'; variant: string; text: string }
  | { type: 'paragraph'; text: string }
  | { type: 'table'; headers: string[]; rows: string[][] };

function parseMarkdownBlocks(markdown: string): Block[] {
  const blocks: Block[] = [];
  const lines = markdown.split('\n');
  let i = 0;

  while (i < lines.length) {
    const line = lines[i];

    // 1. Code Blocks: ```lang ... ```
    if (line.trim().startsWith('```')) {
      const language = line.trim().replace(/^```/, '').trim() || 'text';
      const codeLines: string[] = [];
      i++;
      while (i < lines.length && !lines[i].trim().startsWith('```')) {
        codeLines.push(lines[i]);
        i++;
      }
      i++; // Skip closing ```
      blocks.push({
        type: 'code',
        language: language.toLowerCase(),
        code: codeLines.join('\n'),
      });
      continue;
    }

    // 2. Headings: #, ##, ###, ####
    const headingMatch = line.match(/^(#{1,6})\s+(.*)$/);
    if (headingMatch) {
      blocks.push({
        type: 'heading',
        level: headingMatch[1].length,
        text: headingMatch[2].trim(),
      });
      i++;
      continue;
    }

    // 3. Alerts: > [!NOTE] or > ...
    if (line.trim().startsWith('>')) {
      const alertLines: string[] = [];
      let variant = 'NOTE';
      while (i < lines.length && lines[i].trim().startsWith('>')) {
        let clean = lines[i].trim().replace(/^>\s*/, '');
        if (clean.startsWith('[!')) {
          const match = clean.match(/\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]/i);
          if (match) {
            variant = match[1].toUpperCase();
            clean = clean.replace(/\[![^\]]+\]\s*/, '');
          }
        }
        if (clean) alertLines.push(clean);
        i++;
      }
      blocks.push({
        type: 'alert',
        variant,
        text: alertLines.join(' '),
      });
      continue;
    }

    // 4. Bullet lists: - item, * item
    if (/^\s*[-*]\s+/.test(line)) {
      const items: string[] = [];
      while (i < lines.length && /^\s*[-*]\s+/.test(lines[i])) {
        items.push(lines[i].replace(/^\s*[-*]\s+/, '').trim());
        i++;
      }
      blocks.push({ type: 'bullet', items });
      continue;
    }

    // 5. Numbered lists: 1. item
    if (/^\s*\d+\.\s+/.test(line)) {
      const items: string[] = [];
      while (i < lines.length && /^\s*\d+\.\s+/.test(lines[i])) {
        items.push(lines[i].replace(/^\s*\d+\.\s+/, '').trim());
        i++;
      }
      blocks.push({ type: 'numbered', items });
      continue;
    }

    // 6. Tables: | Header | Header |
    if (line.trim().startsWith('|') && line.trim().endsWith('|')) {
      const tableLines: string[] = [];
      while (i < lines.length && lines[i].trim().startsWith('|')) {
        tableLines.push(lines[i].trim());
        i++;
      }
      if (tableLines.length >= 2) {
        const parseRow = (r: string) =>
          r
            .split('|')
            .slice(1, -1)
            .map((c) => c.trim());
        const headers = parseRow(tableLines[0]);
        // Skip separator line |---|---|
        const rows = tableLines.slice(2).map(parseRow);
        blocks.push({ type: 'table', headers, rows });
        continue;
      }
    }

    // 7. Regular paragraph / empty line
    if (line.trim()) {
      blocks.push({ type: 'paragraph', text: line.trim() });
    }
    i++;
  }

  return blocks;
}

// -------------------------------------------------------------
// BLOCK RENDERER
// -------------------------------------------------------------
function renderBlock(block: Block, index: number) {
  switch (block.type) {
    case 'heading': {
      const style =
        block.level === 1
          ? styles.h1
          : block.level === 2
          ? styles.h2
          : block.level === 3
          ? styles.h3
          : styles.h4;
      return (
        <View style={styles.headingWrap} key={index}>
          <Text style={style}>{renderInline(block.text)}</Text>
        </View>
      );
    }

    case 'code':
      return <CodeBlock key={index} code={block.code} language={block.language} />;

    case 'bullet':
      return (
        <View style={styles.listContainer} key={index}>
          {block.items.map((item, idx) => (
            <View style={styles.listItemRow} key={idx}>
              <Text style={styles.bulletDot}>•</Text>
              <Text style={styles.listText}>{renderInline(item)}</Text>
            </View>
          ))}
        </View>
      );

    case 'numbered':
      return (
        <View style={styles.listContainer} key={index}>
          {block.items.map((item, idx) => (
            <View style={styles.listItemRow} key={idx}>
              <Text style={styles.numberIndex}>{idx + 1}.</Text>
              <Text style={styles.listText}>{renderInline(item)}</Text>
            </View>
          ))}
        </View>
      );

    case 'alert':
      return (
        <View style={styles.alertContainer} key={index}>
          <Feather name="info" size={14} color="#4F46E5" style={styles.alertIcon} />
          <View style={styles.alertContent}>
            <Text style={styles.alertTitle}>{block.variant}</Text>
            <Text style={styles.alertText}>{renderInline(block.text)}</Text>
          </View>
        </View>
      );

    case 'table':
      return (
        <View style={styles.tableContainer} key={index}>
          <View style={styles.tableHeaderRow}>
            {block.headers.map((h, hIdx) => (
              <Text style={styles.tableHeaderCell} key={hIdx}>
                {h}
              </Text>
            ))}
          </View>
          {block.rows.map((row, rIdx) => (
            <View
              style={[styles.tableRow, rIdx % 2 === 1 && styles.tableRowAlt]}
              key={rIdx}
            >
              {row.map((cell, cIdx) => (
                <Text style={styles.tableCell} key={cIdx}>
                  {renderInline(cell)}
                </Text>
              ))}
            </View>
          ))}
        </View>
      );

    case 'paragraph':
      return (
        <Text style={styles.paragraph} key={index}>
          {renderInline(block.text)}
        </Text>
      );

    default:
      return null;
  }
}

// -------------------------------------------------------------
// INLINE PARSER & RENDERER
// -------------------------------------------------------------
function renderInline(text: string): React.ReactNode[] {
  const tokens = parseInline(text);
  return tokens.map((t, idx) => {
    switch (t.type) {
      case 'bold':
        return (
          <Text style={styles.bold} key={idx}>
            {t.text}
          </Text>
        );
      case 'italic':
        return (
          <Text style={styles.italic} key={idx}>
            {t.text}
          </Text>
        );
      case 'code':
        return (
          <Text style={styles.inlineCode} key={idx}>
            {t.text}
          </Text>
        );
      case 'math':
        return (
          <Text style={styles.math} key={idx}>
            {t.text}
          </Text>
        );
      case 'link':
        return (
          <Text
            style={styles.link}
            key={idx}
            onPress={() => Linking.openURL(t.url)}
          >
            {t.text}
          </Text>
        );
      default:
        return t.text;
    }
  });
}

function parseInline(raw: string): InlineToken[] {
  const tokens: InlineToken[] = [];
  let remaining = raw;

  // Regex patterns
  // Bold: **text**
  // Italic: *text*
  // Code: `code`
  // Link: [text](url)
  // Math: $math$
  const regex = /(\*\*([^*]+)\*\*|\*([^*]+)\*|`([^`]+)`|\[([^\]]+)\]\(([^)]+)\)|\$([^$]+)\$)/;

  while (remaining) {
    const match = remaining.match(regex);
    if (!match || match.index === undefined) {
      tokens.push({ type: 'text', text: remaining });
      break;
    }

    if (match.index > 0) {
      tokens.push({ type: 'text', text: remaining.substring(0, match.index) });
    }

    const full = match[0];
    if (full.startsWith('**') && full.endsWith('**')) {
      tokens.push({ type: 'bold', text: match[2] });
    } else if (full.startsWith('*') && full.endsWith('*')) {
      tokens.push({ type: 'italic', text: match[3] });
    } else if (full.startsWith('`') && full.endsWith('`')) {
      tokens.push({ type: 'code', text: match[4] });
    } else if (full.startsWith('[') && full.includes('](')) {
      tokens.push({ type: 'link', text: match[5], url: match[6] });
    } else if (full.startsWith('$') && full.endsWith('$')) {
      tokens.push({ type: 'math', text: match[7] });
    }

    remaining = remaining.substring(match.index + full.length);
  }

  return tokens;
}

// -------------------------------------------------------------
// CODE BLOCK COMPONENT WITH COPY & SYNTAX HIGHLIGHTING
// -------------------------------------------------------------
function CodeBlock({ code, language }: { code: string; language: string }) {
  const [copied, setCopied] = useState(false);

  const handleCopy = () => {
    if (Platform.OS === 'web' && typeof navigator !== 'undefined' && navigator.clipboard) {
      navigator.clipboard.writeText(code);
    }
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const highlightedLines = highlightSyntax(code, language);

  return (
    <View style={styles.codeContainer}>
      <View style={styles.codeHeader}>
        <Text style={styles.codeLangBadge}>{language.toUpperCase()}</Text>
        <TouchableOpacity style={styles.copyBtn} onPress={handleCopy} activeOpacity={0.7}>
          <Feather name={copied ? 'check' : 'copy'} size={12} color={copied ? '#10B981' : '#94A3B8'} />
          <Text style={[styles.copyBtnText, copied && styles.copyBtnSuccess]}>
            {copied ? 'Copied!' : 'Copy'}
          </Text>
        </TouchableOpacity>
      </View>
      <View style={styles.codeBody}>
        {highlightedLines.map((lineTokens, lIdx) => (
          <Text style={styles.codeLine} key={lIdx}>
            {lineTokens.map((tok, tIdx) => (
              <Text key={tIdx} style={{ color: tok.color }}>
                {tok.text}
              </Text>
            ))}
          </Text>
        ))}
      </View>
    </View>
  );
}

// Lightweight syntax highlighter for Python, C, C++, Java, JS, HTML, CSS
interface SyntaxToken {
  text: string;
  color: string;
}

function highlightSyntax(code: string, language: string): SyntaxToken[][] {
  const lines = code.split('\n');
  const lang = language.toLowerCase();

  const keywords = new Set([
    'def', 'class', 'import', 'from', 'return', 'if', 'else', 'elif', 'for', 'while',
    'try', 'except', 'finally', 'with', 'as', 'lambda', 'yield', 'async', 'await',
    'int', 'char', 'float', 'double', 'void', 'include', 'struct', 'typedef', 'sizeof',
    'const', 'static', 'public', 'private', 'protected', 'function', 'let', 'const', 'var',
  ]);

  return lines.map((line) => {
    if (line.trim().startsWith('#') || line.trim().startsWith('//')) {
      return [{ text: line, color: '#64748B' }]; // Gray comment
    }

    const tokens: SyntaxToken[] = [];
    const parts = line.split(/(\s+|[(){}[\];,.<>:+\-*/=!"'])/);

    let inString = false;
    let strQuote = '';

    for (const part of parts) {
      if (!part) continue;

      if ((part === '"' || part === "'") && !inString) {
        inString = true;
        strQuote = part;
        tokens.push({ text: part, color: '#34D399' }); // Green string
        continue;
      }

      if (inString) {
        tokens.push({ text: part, color: '#34D399' });
        if (part === strQuote) inString = false;
        continue;
      }

      if (keywords.has(part)) {
        tokens.push({ text: part, color: '#818CF8' }); // Indigo keyword
      } else if (/^\d+$/.test(part)) {
        tokens.push({ text: part, color: '#FBBF24' }); // Amber number
      } else if (part.includes('(')) {
        tokens.push({ text: part, color: '#F472B6' }); // Pink function
      } else {
        tokens.push({ text: part, color: '#E2E8F0' }); // White/Slate text
      }
    }

    return tokens.length > 0 ? tokens : [{ text: ' ', color: '#E2E8F0' }];
  });
}

// -------------------------------------------------------------
// STYLES
// -------------------------------------------------------------
const styles = StyleSheet.create({
  container: {
    gap: 8,
  },
  userText: {
    color: '#FFFFFF',
    fontSize: 13,
    lineHeight: 19,
  },
  headingWrap: {
    marginTop: 6,
    marginBottom: 2,
  },
  h1: {
    fontSize: 16,
    fontWeight: '800',
    color: '#0F172A',
  },
  h2: {
    fontSize: 15,
    fontWeight: '700',
    color: '#1E293B',
  },
  h3: {
    fontSize: 14,
    fontWeight: '700',
    color: '#334155',
  },
  h4: {
    fontSize: 13,
    fontWeight: '700',
    color: '#475569',
  },
  paragraph: {
    fontSize: 13,
    lineHeight: 20,
    color: '#1E293B',
  },
  bold: {
    fontWeight: '700',
    color: '#0F172A',
  },
  italic: {
    fontStyle: 'italic',
  },
  inlineCode: {
    backgroundColor: '#F1F5F9',
    color: '#4F46E5',
    fontFamily: Platform.OS === 'ios' ? 'Menlo' : 'monospace',
    fontSize: 12,
    paddingHorizontal: 4,
    paddingVertical: 1,
    borderRadius: 4,
    borderWidth: 1,
    borderColor: '#E2E8F0',
  },
  math: {
    fontStyle: 'italic',
    color: '#0F172A',
    fontFamily: Platform.OS === 'ios' ? 'Georgia' : 'serif',
  },
  link: {
    color: '#2563EB',
    textDecorationLine: 'underline',
    fontWeight: '600',
  },

  // Lists
  listContainer: {
    gap: 4,
    paddingLeft: 4,
  },
  listItemRow: {
    flexDirection: 'row',
    alignItems: 'flex-start',
    gap: 6,
  },
  bulletDot: {
    fontSize: 14,
    color: '#4F46E5',
    lineHeight: 20,
  },
  numberIndex: {
    fontSize: 12,
    fontWeight: '700',
    color: '#4F46E5',
    lineHeight: 20,
  },
  listText: {
    flex: 1,
    fontSize: 13,
    lineHeight: 20,
    color: '#1E293B',
  },

  // Alerts
  alertContainer: {
    backgroundColor: '#EEF2FF',
    borderLeftWidth: 3,
    borderLeftColor: '#4F46E5',
    borderRadius: 6,
    padding: 10,
    flexDirection: 'row',
    gap: 8,
    marginVertical: 4,
  },
  alertIcon: {
    marginTop: 2,
  },
  alertContent: {
    flex: 1,
  },
  alertTitle: {
    fontSize: 11,
    fontWeight: '800',
    color: '#4F46E5',
    textTransform: 'uppercase',
    marginBottom: 2,
  },
  alertText: {
    fontSize: 12,
    lineHeight: 18,
    color: '#1E293B',
  },

  // Code Blocks
  codeContainer: {
    backgroundColor: '#0F172A',
    borderRadius: 8,
    borderWidth: 1,
    borderColor: '#1E293B',
    overflow: 'hidden',
    marginVertical: 6,
  },
  codeHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    backgroundColor: '#1E293B',
    paddingHorizontal: 12,
    paddingVertical: 6,
    borderBottomWidth: 1,
    borderBottomColor: '#334155',
  },
  codeLangBadge: {
    fontSize: 10,
    fontWeight: '700',
    color: '#94A3B8',
    letterSpacing: 0.5,
  },
  copyBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 4,
    paddingHorizontal: 6,
    paddingVertical: 2,
    borderRadius: 4,
    backgroundColor: 'rgba(255,255,255,0.06)',
  },
  copyBtnText: {
    fontSize: 10,
    color: '#94A3B8',
    fontWeight: '600',
  },
  copyBtnSuccess: {
    color: '#10B981',
  },
  codeBody: {
    padding: 10,
    overflow: 'scroll',
  },
  codeLine: {
    fontFamily: Platform.OS === 'ios' ? 'Menlo' : 'monospace',
    fontSize: 12,
    lineHeight: 18,
  },

  // Tables
  tableContainer: {
    borderWidth: 1,
    borderColor: '#E2E8F0',
    borderRadius: 6,
    overflow: 'hidden',
    marginVertical: 6,
  },
  tableHeaderRow: {
    flexDirection: 'row',
    backgroundColor: '#F1F5F9',
    borderBottomWidth: 1,
    borderBottomColor: '#CBD5E1',
    padding: 6,
  },
  tableHeaderCell: {
    flex: 1,
    fontSize: 11,
    fontWeight: '700',
    color: '#1E293B',
  },
  tableRow: {
    flexDirection: 'row',
    padding: 6,
    borderBottomWidth: 1,
    borderBottomColor: '#F1F5F9',
  },
  tableRowAlt: {
    backgroundColor: '#F8FAFC',
  },
  tableCell: {
    flex: 1,
    fontSize: 11,
    color: '#334155',
  },
});

